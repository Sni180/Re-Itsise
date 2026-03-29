from django.contrib import admin
from django.urls import path, include

# Import specific functions from your apps
from fault_reporter.views import report
from map.views import about, help_faq
from map import views  # Combined these for cleanliness

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # This includes everything in map/urls.py (like your home/map page)
    path('', include('map.urls')), 
    
    # Direct paths to your pages
    path('report/', report, name='report'),
    path('about/', about, name='about'),  
    path('help/', help_faq, name='help'),
    path('affected/', views.im_affected, name='im_affected'),
    
   
    
]
