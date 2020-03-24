# coding=utf-8
from django import forms


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
        # ('business', 'Юр.Лицо'),
        # ('business_ip', 'ИП'),
    ]
    type = forms.CharField(
        label=u'Тип пользователя',
        widget=forms.Select(choices=USER_TYPES),
        initial=USER_TYPES[0])
