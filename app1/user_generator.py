# coding=utf-8
from random import choice
from string import digits

CYRILIC_LOWERCASE = u'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


class Address(object):
    def __init__(self, name, geo_lat, geo_lon):
        self.name = name
        self.geo_lat = geo_lat
        self.geo_lon = geo_lon


address_list = [
    Address(
        "634061, Томск, Томская область, Сибирская улица, 27",
        "56.481936",
        "84.972976"
    ),
    Address(
        "634034, Томск, Томская область, улица Нахимова, 20/1",
        "56.455235",
        "84.966317"),
    Address(
        "634031, Томск, Томская область, улица Нарановича, 1",
        "56.492649",
        "85.052072"),
    Address(
        "634028, Томск, Томская область, проспект Ленина, 12/1",
        "56.460366",
        "84.950977"),
    Address(
        "634055, Томск, Томская область, Академический проспект, 5",
        "56.473457",
        "85.046689"),
    Address(
        "634041, Томск, Томская область, улица Дзержинского, 12/42",
        "56.472387",
        "84.968979"),
    Address(
        "634061, Томск, Томская область, Киевская улица, 26",
        "56.480519",
        "84.976165"),
]


def private_user_with_phone():
    payloads = ''.join(choice(CYRILIC_LOWERCASE) for _ in range(12))
    phone_payloads = ''.join(choice(digits) for _ in range(7))
    phone = "+7913{}".format(phone_payloads)
    firstname = "Ибрагим-{}".format(payloads.encode('utf-8'))
    lastname = "ЯТебяНайдуЭ-{}".format(payloads.encode('utf-8'))
    password = "qwer1234"
    address_item = choice(address_list)
    return {
        "phone": phone,
        "firstname": firstname,
        "lastname": lastname,
        "password": password,
        "address_name": address_item.name,
        "address_geo_lat": address_item.geo_lat,
        "address_geo_lon": address_item.geo_lon
    }


def private_user_with_email():
    payloads = ''.join(choice(CYRILIC_LOWERCASE) for _ in range(12))
    phone_payloads = ''.join(choice(digits) for _ in range(7))
    firstname = "Ибрагим-{}".format(payloads.encode('utf-8'))
    lastname = "ЯТебяНайдуЭ-{}".format(payloads.encode('utf-8'))
    password = "qwer1234"
    email = "test-{}@remove.com".format(phone_payloads)
    address_item = choice(address_list)
    return {
         "email": email,
        "firstname": firstname,
        "lastname": lastname,
        "password": password,
        "address_name": address_item.name,
        "address_geo_lat": address_item.geo_lat,
        "address_geo_lon": address_item.geo_lon
    }


def private_user_with_phone_email():
    payloads = ''.join(choice(CYRILIC_LOWERCASE) for _ in range(12))
    phone_payloads = ''.join(choice(digits) for _ in range(7))
    phone = "+7913{}".format(phone_payloads)
    firstname = "Ибрагим-{}".format(payloads.encode('utf-8'))
    lastname = "ЯТебяНайдуЭ-{}".format(payloads.encode('utf-8'))
    password = "qwer1234"
    email = "test-{}@remove.com".format(phone_payloads)
    address_item = choice(address_list)
    return {
        "phone": phone,
        "email": email,
        "firstname": firstname,
        "lastname": lastname,
        "password": password,
        "address_name": address_item.name,
        "address_geo_lat": address_item.geo_lat,
        "address_geo_lon": address_item.geo_lon
    }