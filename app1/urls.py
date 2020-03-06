from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ping),
    url(r'^stand/([\\.\w-]+)$', views.set_stand),
    url(r'^create_user/(private_phone_login)$', views.create_user),
    url(r'^create_user/(private_email_login)$', views.create_user),
    url(r'^create_user/(private_phone_email_login)$', views.create_user),
    url(r'^create_user/(business)$', views.create_user),
    url(r'^get_phone_code/(\d+)$', views.get_phone_code),

    url(r'^reset_session/([\w-]+)$', views.bmp_reset_session),
    url(r'^reset_session/([\w-]+),?([\w-]+)$', views.bmp_reset_session),
    url(r'^reset_address_coordinates/(\d+)$', views.reset_address_coordinates),
    url(r'^bmp/db_port$', views.bmp_db_port_old),
    url(r'^db_port$', views.bmp_db_port_old),
    url(r'^db-port/([\\.\w-]+)$', views.bmp_db_port),
]
