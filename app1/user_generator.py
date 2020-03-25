# coding=utf-8
from random import choice
from string import digits

CYRILIC_LOWERCASE = u'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


class Address(object):
    def __init__(self, name, geo_lat, geo_lon):
        self.name = name
        self.geo_lat = geo_lat
        self.geo_lon = geo_lon


inn_list = [
    '928136486703',
    '182783694585',
    '215159451103',
    '871802510759',
    '652787262809',
    '728105086971',
    '158244216123',
    '255183906808',
    '885114954475',
    '723080221899',
    '336811432803',
    '721495683960',
    '233506118864',
    '218104386475',
    '324805516406',
    '552862820636',
    '239705257574',
    '481033033990',
    '502221815111',
    '302302050585',
    '192647702064',
    '379217691698',
    '824008101002',
    '752053132943',
    '334792951684',
    '440236994906',
    '389246336013',
    '629805561237',
    '297599638241',
    '158331239977',
]


def private_user_with_phone(address_count):
    payloads = ''.join(choice(CYRILIC_LOWERCASE) for _ in range(12))
    phone_payloads = ''.join(choice(digits) for _ in range(7))
    phone = "+7913{}".format(phone_payloads)
    firstname = "Ибрагим-{}".format(payloads.encode('utf-8'))
    lastname = "ЯТебяНайдуЭ-{}".format(payloads.encode('utf-8'))
    password = "qwer1234"
    return {
        "phone": phone,
        "firstname": firstname,
        "lastname": lastname,
        "password": password,
        "address_count": address_count,
    }


def private_user_with_email(address_count):
    payloads = ''.join(choice(CYRILIC_LOWERCASE) for _ in range(12))
    phone_payloads = ''.join(choice(digits) for _ in range(7))
    firstname = "Ибрагим-{}".format(payloads.encode('utf-8'))
    lastname = "ЯТебяНайдуЭ-{}".format(payloads.encode('utf-8'))
    password = "qwer1234"
    email = "test-{}@remove.com".format(phone_payloads)
    return {
        "email": email,
        "firstname": firstname,
        "lastname": lastname,
        "password": password,
        "address_count": address_count,
    }


def private_user_with_phone_email(address_count):
    payloads = ''.join(choice(CYRILIC_LOWERCASE) for _ in range(12))
    phone_payloads = ''.join(choice(digits) for _ in range(7))
    phone = "+7913{}".format(phone_payloads)
    firstname = "Ибрагим-{}".format(payloads.encode('utf-8'))
    lastname = "ЯТебяНайдуЭ-{}".format(payloads.encode('utf-8'))
    password = "qwer1234"
    email = "test-{}@remove.com".format(phone_payloads)
    return {
        "phone": phone,
        "email": email,
        "firstname": firstname,
        "lastname": lastname,
        "password": password,
        "address_count": address_count,
    }


def individual_user(address_count, address_not_confirmed_count):
    payloads = ''.join(choice(CYRILIC_LOWERCASE) for _ in range(12))
    phone_payloads = ''.join(choice(digits) for _ in range(7))
    phone = "+7913{}".format(phone_payloads)
    firstname = "Карабас-{}".format(payloads.encode('utf-8'))
    lastname = "Барабасов-{}".format(payloads.encode('utf-8'))
    contractor_name = "ИП {} {}".format(lastname, firstname)
    password = "qwer1234"
    email = "test-individual-{}@remove.com".format(phone_payloads)
    return {
        "firstname": firstname,
        "lastname": lastname,
        "contractor_name": contractor_name,
        "phone": phone,
        "email": email,
        "is_email_verified": "true",
        "address_count": address_count,
        "address_not_confirmed_count": address_not_confirmed_count,
        "inn": choice(inn_list),
        "password": password,
    }


def get_user_and_template(user_type, login_mode, address_count, address_not_confirmed_count):
    user = None
    if user_type == 'individual':
        user = individual_user(address_count, address_not_confirmed_count)
    elif user_type == 'private':
        if login_mode == 'with_phone':
            user = private_user_with_phone(address_count)
        elif login_mode == 'with_email':
            user = private_user_with_email(address_count)
        elif login_mode == 'with_phone_email':
            user = private_user_with_phone_email(address_count)
    return user, "{}_user_{}.sql".format(user_type, login_mode)
