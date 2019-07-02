# coding=utf-8

import re
import requests
import json
from random import choice
from string import ascii_lowercase, digits

jsonify = json.loads

address_list = [
    {
        "title": "634061, Томск, Томская область, Сибирская улица, 27",
        "lat": "56.481936",
        "lon": "84.972976"},
    {
        "title": "634034, Томск, Томская область, улица Нахимова, 20/1",
        "lat": "56.455235",
        "lon": "84.966317"},
    {
        "title": "634031, Томск, Томская область, улица Нарановича, 1",
        "lat": "56.492649",
        "lon": "85.052072"},
    {
        "title": "634028, Томск, Томская область, проспект Ленина, 12/1",
        "lat": "56.460366",
        "lon": "84.950977"},
    {
        "title": "634055, Томск, Томская область, Академический проспект, 5",
        "lat": "56.473457",
        "lon": "85.046689"},
    {
        "title": "634041, Томск, Томская область, улица Дзержинского, 12/42",
        "lat": "56.472387",
        "lon": "84.968979"},
    {
        "title": "634061, Томск, Томская область, Киевская улица, 26",
        "lat": "56.480519",
        "lon": "84.976165"},
]


class QaJsonApi(object):

    def __init__(self, stand):
        self.cyrilic_lowercase = u'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        self.stand = stand
        self.host = "http://api.%s.bmp.dev.magonline.ru" % stand
        self.token = self.get_token()
        self.login_as_admin()
        self.user = None

    def get_token(self):
        response = requests.get("%s/api/auth/token" % self.host)
        return response.headers["Token"]

    def login_as_admin(self):
        self.check_token()

        QA_HEADERS = {"Token": self.token,
                      "Content-Type": "application/json"}
        data = {
            "data": {
                "attributes": {
                    "login": "admin",
                    "password": "admin"
                }
            }
        }
        response = requests.post("%s/api/auth" % self.host, data=json.dumps(data), headers=QA_HEADERS)
        return response.status_code == 204

    def create_private_user(self, phone_as_login=True):
        self.check_token()

        QA_HEADERS = {"Token": self.token,
                      "Content-Type": "application/json"}
        if self.user:
            phone = self.user["phone"]
            firstname = self.user["firstname"]
            lastname = self.user["lastname"]
            password = self.user["password"]
            email = self.user["email"]
        else:
            payloads = ''.join(choice(self.cyrilic_lowercase) for _ in range(12))
            phone = "+7913{}".format(''.join(choice(digits) for _ in range(7)))
            firstname = "Святослав-{}".format(payloads.encode('utf-8'))
            lastname = "Колесников-{}".format(payloads.encode('utf-8'))
            password = "qwer1234"
            email = "test-{}@test.ru".format(''.join(choice(digits) for _ in range(7)))
        address_item = choice(address_list)
        data = {
            "data": {
                "attributes": {
                    "name": "Физическое лицо",
                    "is_active": True,
                    "type": "physical",
                    "status": "confirmed"
                },
                "relationships": {
                    "delivery-addresses": {
                        "data": [
                            {
                                "attributes": {
                                    "is_active": True,
                                    "status": 2,
                                    "geo": {
                                        "longitude": address_item["lon"],
                                        "latitude": address_item["lat"]
                                    },
                                    "address": address_item["title"],
                                    "contact_phone": phone,
                                    "contact_firstname": firstname,
                                    "contact_lastname": lastname,
                                    "comment": "Коммент_к_адресу_доставки_тест",
                                    "is_default": True
                                }
                            }
                        ]
                    }
                }
            }
        }
        response = requests.post("%s/api/contractors" % self.host, data=json.dumps(data), headers=QA_HEADERS)
        content = jsonify(response.content.decode('utf-8'))
        contractor_id = content["data"]["id"] if "data" in content else None
        if not contractor_id:
            raise Exception("Contractor ID is not created")
        data = {
            "data": {
                "attributes": {
                    "first_name": firstname,
                    "last_name": lastname,
                    "is_phone_verified": True,
                    "phone": phone,
                    "email": email,
                    "is_email_verified": True if email else False,
                    "is_active": True,
                    "contractor_id": contractor_id
                },
                "relationships": {
                    "user-roles": {
                        "data": [
                            {
                                "attributes": {
                                    "role_name": "member"
                                }
                            }
                        ]
                    },
                    "identities": {
                        "data": {
                            "attributes": {
                                "identity": phone if phone_as_login else email,
                                "open_credential": password
                            }
                        }
                    }
                }
            }
        }
        response = requests.post("%s/api/users" % self.host, data=json.dumps(data), headers=QA_HEADERS)
        content = jsonify(response.content.decode('utf-8'))
        user_id = content["data"]["id"] if content.has_key("data") else None
        if response.status_code == 201:
            return {
                "id": user_id,
                "firstname": firstname,
                "lastname": lastname,
                "phone": phone,
                "email": email,
                "password": "qwer1234",
                "address": address_item
            }
        else:
            raise Exception(content)

    def check_token(self):
        if not self.token:
            raise Exception("Token is missing")

    def set_user(self, data):
        self.user = data

# if __name__ == '__main__':
# create_private_user("asdasd")
# if login_as_admin(get_token()):
#     print "Login good!"
# else:
#     print "Login failed"
