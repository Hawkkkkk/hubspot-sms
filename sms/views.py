from django.shortcuts import render
import requests
# Create your views here.
def send_sms(request):
    return render(request, "home.html")