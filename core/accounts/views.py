from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from time import sleep
from .tasks import sendEmail
import requests


def send_email(request):
    sendEmail.delay()
    return HttpResponse("<h1>Done Sending Email</h1>")

# def cache_test(request):
#     if cache.get("test_delay_api") is None:
#         response = requests.get("https://api.persian-calendar.ir/api/v1/calendar/get-year/1405", verify=False)
#         cache.set("test_delay_api", response.json(),60)
#     return JsonResponse(cache.get("test_delay_api"))

@cache_page(60)
def cache_test(request):
    response = requests.get("https://api.persian-calendar.ir/api/v1/calendar/get-year/1405", verify=False)

    return JsonResponse(response.json())
