from django.contrib import admin
from .models import Fault

from django.contrib import admin
from .models import Fault

@admin.register(Fault)
class FaultAdmin(admin.ModelAdmin):
    # 1. This controls what you see in the table list view
    list_display = ('ref_number', 'category', 'status', 'date_reported', 'full_name')
    
    # 2. This makes the user-submitted data READ-ONLY for the Admin
    # This prevents municipal staff from changing the citizen's evidence
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

    # 3. This organizes the page so the Admin can ONLY change the Status
    fieldsets = (
        ('Municipal Action', {
            'fields': ('status',)  # The only editable field
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

    # Optional: adds a filter on the right side to find faults by status
    list_filter = ('status', 'category')