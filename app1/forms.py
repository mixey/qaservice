# coding=utf-8
from django import forms
import re


class ResetTokenForm(forms.Form):
    RESET_MODES = [
        ('remove', 'Удалить'),
        ('logout', 'Разлогинить'),
    ]
    token = forms.CharField()
    refresh_token = forms.CharField(required=False)
    reset_mode = forms.CharField(
        label=u'Применить режим',
        widget=forms.Select(choices=RESET_MODES),
        required=False,
        initial=RESET_MODES[0])


class UserKindForm(forms.Form):
    USER_TYPES = [
        ('private', 'Физ.Лицо'),
        ('individual', 'ИП'),
        # ('business', 'Юр.Лицо'),
    ]
    ACCOUNT_MODES = [
        ('with_phone', 'По телефону'),
        ('with_email', 'По Email'),
        ('with_phone_email', 'По Телефону и Email'),
    ]
    type = forms.CharField(
        label=u'Тип пользователя',
        widget=forms.Select(choices=USER_TYPES),
        initial=USER_TYPES[0])
    city = forms.CharField(disabled=True, initial='Томск', label=u'Город')
    login_mode = forms.CharField(
        label=u'Аккаунт',
        widget=forms.Select(choices=ACCOUNT_MODES),
        initial=ACCOUNT_MODES[0])
    address_count = forms.CharField(initial=1, label=u'Количество адресов(Торговых точек)')
    address_not_confirmed_count = forms.CharField(initial=0,
                                                  label=u'Количество не подтвержденных адресов(Торговых точек)')

    def clean(self):
        cleaned_data = super(UserKindForm, self).clean()
        user_type = cleaned_data.get("type")
        address_count = cleaned_data.get("address_count")
        address_not_confirmed_count = cleaned_data.get("address_not_confirmed_count")
        login_mode = cleaned_data.get("login_mode")

        if address_count or address_not_confirmed_count:
            msg = u"Значение может содержать только цифры 0-9, меньше 20"
            if not re.findall("^\\d{0,2}$", address_count):
                self.add_error('address_count', msg)
            if not re.findall("^\\d{0,2}$", address_not_confirmed_count):
                self.add_error('address_not_confirmed_count', msg)

        if user_type and address_not_confirmed_count and not self.has_error('address_not_confirmed_count'):
            if user_type == 'private' and int(address_not_confirmed_count) > 0:
                msg = u"Для этого типа поль-теля нельзя использовать этот параметр"
                self.add_error('address_not_confirmed_count', msg)
        if user_type and login_mode:
            if user_type == 'individual' and login_mode in ['with_phone', 'with_phone_email']:
                msg = u"Для этого типа поль-теля нельзя использовать этот параметр"
                self.add_error('login_mode', msg)
