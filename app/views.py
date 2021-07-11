from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Hello World!')


def my_date(request, year, month, day):
    return HttpResponse(str(year)+'/'+str(month)+'/'+str(day))


# Create your views here.
def app_view(request):
    return HttpResponse("Hello 2021")

