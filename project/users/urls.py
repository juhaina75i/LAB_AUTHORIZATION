from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('signup/' , user_signup , name='signup'),
    path('login/' , user_login , name='login'),
    path('logout/' , logout , name='logout'),
]
