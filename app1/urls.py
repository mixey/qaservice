from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ping),
    url(r'stand/([\.\w-]+)$', views.set_stand),
    url(r'reset_session/(\w+)$', views.reset_session),
    url(r'reset_recovery_requests$', views.reset_recovery_requests),
    url(r'create_user/(\w+)$', views.create_user),
    url(r'create_all$', views.create_all),
]
