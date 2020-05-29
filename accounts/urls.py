from django.urls import path
from django.conf.urls import url
from . import views


app_name = 'accounts'

urlpatterns = [
		path('registration', views.registration, name='registration'),
		path('login',views.login,name='login'),
		path('logout',views.logout,name='logout'),
		path('password_reset',views.password_reset,name='password_reset'),
		url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
		views.activate, name='activate'),

]
