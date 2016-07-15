from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^accounts/login/$', views.login, name='login_account'),
    url(r'^accounts/register/$', views.register_user, name='new_account'),
    url(r'^accounts/register_success/$', views.register_success, name='register_success'),
    url(r'^accounts/auth/$',  views.auth_view, name='auth_view'),
    url(r'^accounts/loggedin/$',views.loggedin,name='loggedin'),
    url(r'^accounts/invalid/$', views.invalid_login,name='invalid_login'),
    url(r'^accounts/logout/$', views.logout,name='logout'),
]
