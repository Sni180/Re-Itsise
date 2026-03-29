from django.urls import path
from . import views

urlpatterns = [
    path('', views.explorer_map, name='explorer_map'),
    path('about/', views.about, name='about'),
path('help/', views.help_faq, name='help'),
]