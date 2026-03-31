from django.contrib import admin
from .models import Fault, AffectedResident

class AffectedResidentInline(admin.TabularInline):
    model = AffectedResident
    extra = 0  
    
    readonly_fields = ('full_name', 'cellphone', 'date_joined')
    can_delete = False  

@admin.register(Fault)
class FaultAdmin(admin.ModelAdmin):
   
    inlines = [AffectedResidentInline]

    
    list_display = ('ref_number', 'category', 'status', 'date_reported', 'full_name')
    
    
    readonly_fields = (
        'ref_number', 
        'full_name', 
        'cellphone', 
        'category', 
        'location_address', 
        'latitude', 
        'longitude', 
        'description', 
        'image', 
        'audio_report', 
        'date_reported'
    )

    # Mona I'm making sure gore the Admin can ONLY change the  report Status
    fieldsets = (
        ('Municipal Action', {
            'fields': ('status',)  
        }),
        ('Citizen Report Information', {
            'fields': (
                'ref_number', 
                'full_name', 
                'cellphone', 
                'category', 
                'location_address', 
                'description', 
                'image', 
                'audio_report', 
                'date_reported'
            ),
        }),
    )

    
    list_filter = ('status', 'category')