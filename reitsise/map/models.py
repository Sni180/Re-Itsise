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

    # --- AUTO-GENERATED REFERENCE NUMBER ---
    # editable=False hides it from the report form so users can't change it
    ref_number = models.CharField(max_length=10, unique=True, null=True, blank=True, editable=False)
    # Information from Step 1
    full_name = models.CharField(max_length=150)
    cellphone = models.CharField(max_length=15)

    # Information from Step 2
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    location_address = models.TextField()
    latitude = models.DecimalField(max_digits=12, decimal_places=9, null=True, blank=True)
    longitude = models.DecimalField(max_digits=12, decimal_places=9, null=True, blank=True)

    # Information from Step 3 (Evidence)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='fault_images/', null=True, blank=True)
    audio_report = models.FileField(upload_to='fault_audio/', null=True, blank=True)

    # Internal Status Tracking
    status = models.CharField(max_length=10, default='LOG', choices=[
        ('LOG', 'Logged'), 
        ('DIS', 'Dispatched'), 
        ('PROG', 'In Progress'), 
        ('RES', 'Resolved')
    ])
    date_reported = models.DateTimeField(auto_now_add=True)

    # --- THE AUTOMATIC LOGIC ---
    def save(self, *args, **kwargs):
        # Only create a reference number if it doesn't exist yet (new reports)
        if not self.ref_number:
            # Generates a 6-character random code: e.g., RI-8F2D4E
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
        # Including the ref_number makes it easier to find in the Admin
        return f"{self.ref_number} - {self.get_category_display()}"