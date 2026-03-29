from django.db import models

class Fault(models.Model):
    CATEGORY_CHOICES = [
        ('ELEC', '⚡ Electricity'), ('WLEAK', '💧 Water Leak'),
        ('BPIPE', '🌊 Burst Pipe'), ('MHOLE', '🕳️ Missing Manhole'),
        ('RUBBL', '🏗️ Rubble'), ('STORM', '⛈️ Storm Water'),
        ('SANI', '🚽 Sanitation'), ('POTH', '🚧 Pothole'), ('OTHER', '🌳 Other')
    ]

    full_name = models.CharField(max_length=150)
    cellphone = models.CharField(max_length=15)
    category = models.CharField(max_length=5, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True, null=True)
    location_address = models.TextField()
    image = models.ImageField(upload_to='fault_images/', null=True, blank=True)
    
    # These must have numbers for the pin to show up!
    latitude = models.DecimalField(max_digits=12, decimal_places=9, null=True, blank=True)
    longitude = models.DecimalField(max_digits=12, decimal_places=9, null=True, blank=True)

    status = models.CharField(max_length=4, default='LOG', choices=[
        ('LOG', 'Logged'), ('DIS', 'Dispatched'), ('PROG', 'In Progress'), ('RES', 'Resolved')
    ])
    date_reported = models.DateTimeField(auto_now_add=True)

    @property
    def icon(self):
        mapping = dict(self.CATEGORY_CHOICES)
        return mapping.get(self.category, '📍').split(' ')[0]

    class Meta:
        ordering = ['-date_reported']

    def __str__(self):
        return f"{self.get_category_display()} - {self.location_address[:30]}"