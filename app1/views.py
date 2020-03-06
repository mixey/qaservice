# -*- coding: utf-8 -*-

import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from app1 import user_generator
from app1.posgresql_executor import PostgreSqlExec
from app1.sql_executor import SqlExec
from app1.ssh_executor import SshExecutor

DEFAULT_STAND = "mobile"


def ping(request):
    return HttpResponse(json.dumps({"message": "OK",
                                    "stand": request.session.get('stand', DEFAULT_STAND),
                                    "data": "You are: {}/{}".format(request.META['REMOTE_ADDR'],
                                                                    request.META['HTTP_USER_AGENT'])}),
                        content_type="application/json; charset=utf-8")


def set_stand(request, stand):
    request.session["stand"] = stand
    return ping(request)


def bmp_reset_session(request, token, refresh_token=None):
    stand = request.session.get('stand', DEFAULT_STAND)

    executor = SshExecutor()
    sql_executor = PostgreSqlExec(stand)
    error = None
    try:
        executor.execute(
            "cd /opt/stand/marketplace/%s \ndc exec -T redis redis-cli -n 0 eval \"return redis.call('del', 'Token:%s')\" 0 prefix" % (
                stand, token))
        if refresh_token:
            executor.execute(
                "cd /opt/stand/marketplace/%s \ndc exec -T redis redis-cli -n 0 eval \"return redis.call('del', 'Token:%s')\" 0 prefix" % (
                    stand, refresh_token))

        sql_executor.execute("delete from user_token where token = '%s';" % token)
        sql_executor.commit()

    except Exception, msg:
        error = msg
    executor.close()
    sql_executor.close()
    response_data = {"message": "OK" if error is None else "'{}'".format(error),
                     "stand": stand,
                     "data": {"reset_token": token, "reset_refresh_token": refresh_token}
                     }
    return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def create_user(request, user_type):
    error = None
    stand = request.session.get('stand', DEFAULT_STAND)
    response_data = {"stand": stand}
    try:
        db_exec = PostgreSqlExec(stand)
        query = None
        user_data = None
        if user_type == "private_phone_login":
            user_data = user_generator.private_user_with_phone()
            query = db_exec.render_template("assets/private_user_with_phone.sql.template", user_data)
        elif user_type == "private_email_login":
            user_data = user_generator.private_user_with_email()
            query = db_exec.render_template("assets/private_user_with_email.sql.template", user_data)
        elif user_type == "private_phone_email_login":
            user_data = user_generator.private_user_with_phone_email()
            query = db_exec.render_template("assets/private_user_with_phone_email.sql.template", user_data)

        db_exec.execute_batch(query)
        db_exec.commit()
        response_data["data"] = user_data

        if not query and not user_data:
            raise Exception("Use following endpoints: private_phone_login, private_email_login, private_phone_email_login" )
    except Exception, ex:
        print ex.message
        error = ex.message
        response_data["error"] = ex.message

    response = HttpResponse(json.dumps(response_data), content_type="application/json")
    if error:
        response.status_code = 400
    return response


def create_all(request):
    stand = request.session.get('stand', DEFAULT_STAND)
    error = None
    executor = SqlExec(stand)
    try:
        executor.exec_file('assets/private_user_with_phone.sql.template')
        executor.exec_file('assets/business_customer.sql')
        executor.commit()
    except Exception, msg:
        error = msg
    executor.close()

    response_data = {"data": "OK" if error is None else "'{}'".format(error),
                     "stand": stand
                     }
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def bmp_db_port(request, stand):
    executor = SshExecutor()
    try:
        result = executor.execute(
            "cd /opt/stand/marketplace/%s && dc ps | grep -Po '(\d+)->5432' | grep -Po '^\d+'" % stand)
    except Exception, msg:
        return HttpResponse(msg)
    executor.close()

    response_data = {"data": result.rstrip('\n'),
                     "stand": stand}
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def bmp_db_port_old(request):
    stand = request.session.get('stand', DEFAULT_STAND)
    return bmp_db_port(request, stand)


def reset_address_coordinates(request, address_id):
    stand = request.session.get('stand', DEFAULT_STAND)
    response_data = {"stand": stand}
    executor = PostgreSqlExec(stand)
    try:
        message = executor.execute_fetch("update delivery_address set geo = null where id = %s;" % address_id)
        executor.commit()
        response_data["data"] = message
    except Exception, error:
        error_result = error.message
        response_data["error"] = error_result
    executor.close()
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def delete_user(request):
    return None


def get_phone_code(request, phone):
    stand = request.session.get('stand', DEFAULT_STAND)
    executor = PostgreSqlExec(stand)
    error_result = None
    result = None
    response_data = {"stand": stand}
    try:
        cursor = executor.execute_fetch("""
            SELECT token
            FROM verification
            WHERE value = '+{}'
            LIMIT 1""".format(phone))
        value_result = cursor[0][0] if cursor else None
        if not value_result:
            raise Exception("Phone ({}) is missing".format(phone))

        cursor = executor.execute_fetch("""
            SELECT token
            FROM verification
            WHERE value = '+{}'
                  AND scenario = 'confirm'
                  AND is_verified = FALSE
            LIMIT 1""".format(phone))
        result = cursor[0][0] if cursor else None
        response_data["data"] = result
    except Exception, error:
        error_result = error.message
        response_data["error"] = error_result
    executor.close()

    return HttpResponse(json.dumps(response_data), content_type="application/json")
