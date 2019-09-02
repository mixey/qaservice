# -*- coding: utf-8 -*-

import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import qa_jsonapi
from app1.posgresql_executor import PostgreSqlExec
from app1.sql_executor import SqlExec
from app1.ssh_executor import SshExecutor


def ping(request):
    return HttpResponse(json.dumps({"message": "OK",
                                    "stand": request.session.get('stand', 'mobile'),
                                    "data": "You are: {}/{}".format(request.META['REMOTE_ADDR'],
                                                                    request.META['HTTP_USER_AGENT'])}),
                        content_type="application/json; charset=utf-8")


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
    stand = request.session.get('stand', 'master')

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


@csrf_exempt
def create_user(request, user_type):
    error = None
    stand = request.session.get('stand', 'mobile')
    response_data = {}
    try:
        if user_type == "private_phone_login" or user_type == "private_email_login":
            api = qa_jsonapi.QaJsonApi(stand)

            if request.body:
                body_unicode = request.body.decode('utf-8')
                body = json.loads(body_unicode)
                api.set_user(body)
            phone_as_login = True if user_type == "private_phone_login" else False
            response_data["data"] = api.create_private_user(phone_as_login)
        else:
            raise Exception("Type value '{}' should be (private)".format(user_type))
    except Exception, ex:
        error = ex.message

    response_data["message"] = "OK" if error is None else error
    response_data["stand"] = stand
    response = HttpResponse(json.dumps(response_data), content_type="application/json")
    if error:
        response.status_code = 400
    return response


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


def bmp_db_port(request, stand):
    executor = SshExecutor(stand, 42344)
    try:
        result = executor.execute(
            "cd /opt/stand/marketplace/%s && dc ps | grep -Po '(\d+)->5432' | grep -Po '^\d+'" % stand)
    except Exception, msg:
        return HttpResponse(msg)
    executor.close()

    return HttpResponse(result)


def bmp_db_port_old(request):
    stand = request.session.get('stand', 'master')
    return bmp_db_port(request, stand)


def reset_address_coordinates(request, address_id):
    stand = request.session.get('stand', 'master')
    message = None
    executor = PostgreSqlExec(stand, 42344)
    try:
        message = executor.execute("update delivery_address set geo = null where id = %s;" % address_id)
        executor.commit()
    except Exception, msg:
        message = msg
    executor.close()
    response_data = {"message": message,
                     "stand": stand}
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def delete_user(request):
    return None


def get_phone_code(request, phone):
    stand = request.session.get('stand', 'master')
    executor = PostgreSqlExec(stand, 42344)
    try:
        cursor = executor.execute("""
            SELECT token
            FROM verification
            WHERE value = '+%s'
                  AND scenario = 'confirm'
                  AND is_verified = FALSE
            LIMIT 1""" % phone)
        code = cursor[0][0] if cursor else None
    except Exception, msg:
        code = msg
    executor.close()
    response_data = {"data": code,
                     "stand": stand}
    return HttpResponse(json.dumps(response_data), content_type="application/json")
    return None
