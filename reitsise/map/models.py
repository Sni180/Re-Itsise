import uuid
from django.db import models

class Fault(models.Model):
    CATEGORY_CHOICES = [
        ('ELEC', '⚡ Electricity'), 
        ('WLEAK', '💧 Water Leak'),
        ('BPIPE', '🌊 Burst Pipe'), 
        ('MHOLE', '🕳️ Missing Manhole'),
        ('RUBBL', '🏗️ Rubble'), 
        ('STORM', '⛈️ Storm Water'),
        ('SANI', '🚽 Sanitation'), 
        ('POTH', '🚧 Pothole'), 
        ('OTHER', '🌳 Other')
    ]

   
    ref_number = models.CharField(max_length=12, unique=True, null=True, blank=True, editable=False)
    
    # Mona I'm storing the user info submitted from Step 1
    full_name = models.CharField(max_length=150)
    cellphone = models.CharField(max_length=15)

    # Mona I'm storing the report category le address  from Step 2
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    location_address = models.TextField()
    latitude = models.DecimalField(max_digits=12, decimal_places=9, null=True, blank=True)
    longitude = models.DecimalField(max_digits=12, decimal_places=9, null=True, blank=True)

    # Mona ke store the report evidence from step 3
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='fault_images/', null=True, blank=True)
    audio_report = models.FileField(upload_to='fault_audio/', null=True, blank=True)

    
    status = models.CharField(max_length=10, default='LOG', choices=[
        ('LOG', 'Logged'), 
        ('DIS', 'Dispatched'), 
        ('PROG', 'In Progress'), 
        ('RES', 'Resolved')
    ])
    date_reported = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.ref_number:
            random_id = uuid.uuid4().hex[:6].upper()
            self.ref_number = f"RI-{random_id}"
        super(Fault, self).save(*args, **kwargs)

    @property
    def icon(self):
        mapping = dict(self.CATEGORY_CHOICES)
        icon_with_text = mapping.get(self.category, '📍')
        return icon_with_text.split(' ')[0]

    class Meta:
        ordering = ['-date_reported']

    def __str__(self):
        return f"{self.ref_number} - {self.get_category_display()}"


class AffectedResident(models.Model):
    """Stores details for residents who click 'I'm Affected Too'"""
    fault = models.ForeignKey(
        Fault, 
        on_delete=models.CASCADE, 
        related_name='affected_residents'
    )
    full_name = models.CharField(max_length=150)
    cellphone = models.CharField(max_length=15)
    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_joined']

    def __str__(self):
        return f"{self.full_name} - {self.fault.ref_number}"