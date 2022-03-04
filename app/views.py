import csv

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Hello World!')


def my_date(request, year, month, day):
    return HttpResponse(str(year)+'/'+str(month)+'/'+str(day))


def my_year(request, year):
    return render(request, 'my_year.html')


def my_year_dict(request, year, month):
    return render(request, 'my_year_dict.html', {'month': month})


def download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    writer = csv.writer(response)
    writer.writerow(['First now', 'A', 'B', 'C'])
    return request


# Create your views here.
def app_view(request):
    return HttpResponse("Hello 2021")

