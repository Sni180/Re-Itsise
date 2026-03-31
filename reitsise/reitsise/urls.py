from django.contrib import admin
from django.urls import path, include


from fault_reporter.views import report
from map.views import about, help_faq
from map import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    
  
    path('', include('map.urls')), 
    
   
    path('report/', report, name='report'),
    path('about/', about, name='about'),  
    path('help/', help_faq, name='help'),
    path('affected/', views.im_affected, name='im_affected'),
    
   
    
]
