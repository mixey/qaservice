# -*- coding: utf-8 -*-

from app1.posgresql_executor import PostgreSqlExec
from app1.ssh_executor import SshExecutor


def remove_token(stand, tokens):
    executor = SshExecutor()
    sql_executor = PostgreSqlExec(stand)
    result = None
    error = None
    try:
        for token in tokens:
            if not token: continue
            executor.execute(
                "cd /opt/stand/marketplace/%s \ndocker-compose exec -T redis redis-cli -n 0 eval \"return redis.call('del', 'Token:%s')\" 0 prefix" % (
                    stand, token))
            sql_executor.execute("delete from user_token where token = '%s';" % token)
        sql_executor.commit()
        result = u"Токен теперь не активный"
    except Exception, msg:
        error = msg
    executor.close()
    sql_executor.close()
    return result, error


def logout_token(stand, tokens):
    executor = SshExecutor()
    sql_executor = PostgreSqlExec(stand)
    result = None
    error = None
    try:
        for token in tokens:
            executor.execute(
                "cd /opt/stand/marketplace/%s \ndocker-compose exec -T redis redis-cli -n 0 eval \"return redis.call('del', 'Token:%s')\" 0 prefix" % (
                    stand, token))
            sql_executor.execute("update user_token set user_profile_id = null where token = '%s';" % token)
        sql_executor.commit()
        result = u"Токены разлогинены"
    except Exception, msg:
        error = msg
    executor.close()
    sql_executor.close()
    return result, error
