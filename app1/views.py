# -*- coding: utf-8 -*-

from django.http import HttpResponse
import json
import time
import datetime

from app1.sql_executor import SqlExec
from app1.test_data import private_data, individual_data, business_data


def ping(request):    
    return HttpResponse(json.dumps({"you_are": "{}/{}".format(request.META['REMOTE_HOST'],
                                                             request.META['HTTP_USER_AGENT']),
                                    "stand": request.session.get('stand', 'mobile')
                                    }), content_type="application/json")


def set_stand(request, stand):
    request.session["stand"] = stand
    return ping(request) 
    
    
def reset_session(request, session_id, timestamp=None):           
    if timestamp is None:
        timestamp = time.mktime((datetime.date.today() - datetime.timedelta(days=30)).timetuple())        
    
    stand = request.session.get('stand', 'mobile')
    sql_command = "update core_session set session_expires = {} where session_id = '{}'".format(int(timestamp), session_id)
    executor = SqlExec(stand)
    error = None
    try: 
        executor.execute(sql_command)
        executor.commit()
    except Exception, msg: 
        error = msg 
    executor.close()
    
    response_data = {"message": "OK" if error is None else "'{}'".format(error),
                     "stand" : stand,
                     "data": {"session_id": session_id,
                              "session_expired": timestamp,
                              "session_expired_str": datetime.datetime.fromtimestamp(float(timestamp)).strftime('%Y-%m-%d %H:%M:%S')}
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
                     "stand" : stand,
                     "data": user}
    return HttpResponse(json.dumps(response_data), content_type="application/json")

    
def create_all(request):
    stand = request.session.get('stand', 'mobile')
    error = None
    executor = SqlExec(stand)    
    try: 
        executor.exec_file('d:/sources/python/magonline/private_customer.sql')
        executor.exec_file('d:/sources/python/magonline/business_customer.sql')
        executor.commit()
    except Exception, msg: 
        error = msg 
    executor.close()
    
    response_data = {"message": "OK" if error is None else "'{}'".format(error),
                     "stand" : stand
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
                     "stand" : stand
                     }
    return HttpResponse(json.dumps(response_data), content_type="application/json")
    