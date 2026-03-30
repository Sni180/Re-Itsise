from django.contrib import admin
from .models import Fault, AffectedResident

# 1. Define the Inline view for Affected Residents
class AffectedResidentInline(admin.TabularInline):
    model = AffectedResident
    extra = 0  # Prevents empty rows from appearing by default
    # Make these read-only so municipal staff can't alter citizen data
    readonly_fields = ('full_name', 'cellphone', 'date_joined')
    can_delete = False  # Staff shouldn't remove people from the affected list

@admin.register(Fault)
class FaultAdmin(admin.ModelAdmin):
    # 2. Add the Inline to the FaultAdmin class
    inlines = [AffectedResidentInline]

    # This controls what you see in the table list view
    list_display = ('ref_number', 'category', 'status', 'date_reported', 'full_name')
    
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

    # This organizes the page so the Admin can ONLY change the Status
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

    # Adds a filter on the right side to find faults by status or category
    list_filter = ('status', 'category')