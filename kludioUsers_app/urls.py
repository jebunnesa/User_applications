from django.urls import path

from . import views

urlpatterns = [
    path('user', views.user, name='user'),
    path('user_form', views.user_form, name='user_form'),
]
