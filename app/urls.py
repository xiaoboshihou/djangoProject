from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index),
    path('<year>/<int:month>/<slug:day>', views.my_date),
    path('download.html', views.download),
    re_path('(?P<year>[0-9]{4}).html', views.my_year, name='my_year'),
    re_path('dict/(?P<year>[0-9]{4}).html', views.my_year_dict, {'month': '05'}, name='my_year_dict')
]

