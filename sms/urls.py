from django.urls import path
from . import views


urlpatterns = [
    path('', views.send_sms, name='send_sms'),
    path('post/', views.send_sms, name='send_sms')
]