# -*- coding: utf-8 -*-

from django.http import HttpResponse
import json
import time
import datetime

from app1.sql_executor import SqlExec
from app1.test_data import private_data, individual_data, business_data
from app1.ssh_executor import SshExecutor


def ping(request):
    return HttpResponse(json.dumps({"you_are": "{}/{}".format(request.META['REMOTE_ADDR'],
                                                              request.META['HTTP_USER_AGENT']),
                                    "stand": request.session.get('stand', 'mobile')
                                    }), content_type="application/json")


def set_stand(request, stand):
    request.session["stand"] = stand
    return ping(request)


def reset_session(request, session_id):
    stand = request.session.get('stand', 'mobile')

    executor = SshExecutor(stand)
    error = None
    try:
        executor.execute(
            "cd /opt/stand/magonline/%s \ndc exec -T sesredis redis-cli -n 2 eval \"return redis.call('del', 'sess_%s')\" 0 prefix" % (
                stand, session_id))
        # executor.execute("cd /opt/stand/magonline/%s \ndc exec -T sesredis bash" % (stand))
    except Exception, msg:
        error = msg
    executor.close()

    response_data = {"message": "OK" if error is None else "'{}'".format(error),
                     "stand": stand,
                     "data": {"session_id": session_id}
                     }
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def bmp_reset_session(request, token, refresh_token=None):
    stand = "master"

    executor = SshExecutor(stand, 42344)
    error = None
    try:
        executor.execute(
            "cd /opt/stand/marketplace/%s \ndc exec -T redis redis-cli -n 0 eval \"return redis.call('del', 'Token:%s')\" 0 prefix" % (
                stand, token))
        if refresh_token:
            executor.execute(
                "cd /opt/stand/marketplace/%s \ndc exec -T redis redis-cli -n 0 eval \"return redis.call('del', 'Token:%s')\" 0 prefix" % (
                    stand, refresh_token))
    except Exception, msg:
        error = msg
    executor.close()

    response_data = {"message": "OK" if error is None else "'{}'".format(error),
                     "stand": stand,
                     "data": {"reset_token": token, "reset_refresh_token": refresh_token}
                     }
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def create_user(request, user_type):
    sql_command = ""
    user = {}
    if user_type == "private":
        sql_command, user = private_data()
    #     elif user_type == "individual":
    #         sql_command, user = individual_data()
    #     elif user_type == "business":
    #         sql_command, user = business_data()
    else:
        raise Exception("Type value '{}' should be (private)".format(user_type))

    stand = request.session.get('stand', 'mobile')
    error = None
    executor = SqlExec(stand)
    try:
        executor.statement(sql_command)
        executor.commit()
    except Exception, msg:
        error = msg
    executor.close()

    response_data = {"message": "OK" if error is None else "'{}'".format(error),
                     "stand": stand,
                     "data": user}
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def create_all(request):
    stand = request.session.get('stand', 'mobile')
    error = None
    executor = SqlExec(stand)
    try:
        executor.exec_file('assets/private_customer.sql')
        executor.exec_file('assets/business_customer.sql')
        executor.commit()
    except Exception, msg:
        error = msg
    executor.close()

    response_data = {"message": "OK" if error is None else "'{}'".format(error),
                     "stand": stand
                     }
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def reset_recovery_requests(request):
    stand = request.session.get('stand', 'mobile')
    error = None
    executor = SqlExec(stand)
    try:
        executor.execute("delete from customer_flowpassword")
        executor.commit()
    except Exception, msg:
        error = msg
    executor.close()
    response_data = {"message": "OK" if error is None else "'{}'".format(error),
                     "stand": stand
                     }
    return HttpResponse(json.dumps(response_data), content_type="application/json")
