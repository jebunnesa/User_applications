from django.urls import path

from . import views

urlpatterns = [
    path('user', views.user, name='user'),
    path('', views.user_form, name='user_form'),
]
