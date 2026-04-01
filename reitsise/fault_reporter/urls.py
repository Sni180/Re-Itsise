from django.contrib import admin
from django.urls import path, include

from reitsise.fault_reporter import views


urlpatterns = [

    path('', views.report , name='report'),
]
