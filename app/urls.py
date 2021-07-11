from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<year>/<int:month>/<slug:day>', views.my_date)
]

