import django.utils.timezone

# from django.contrib.gis.db import models
from django.contrib.gis.db import models

from django.db import models

# Create your models here.
class Donor(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField(default=0)
    zipcode = models.PositiveIntegerField(default = 0)
    latitude = models.DecimalField(max_digits=8, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    # location = django.contrib.gis.db.models.PointField(null=False, blank=False, srid=4326, verbose_name="Location")
    join_date = models.DateTimeField('date joined', default=django.utils.timezone.now)
    points = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.id

    def valid(self):
        return self.quantity > 0

class Recipient(models.Model):
    name = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=200, blank=True)
    request = models.IntegerField(default=1)
    zipcode = models.PositiveIntegerField(default = 0)
    latitude = models.DecimalField(max_digits=8, decimal_places=6, default=0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    # location = django.contrib.gis.db.models.PointField(null=False, blank=False, srid=4326, verbose_name="Location")
    join_date = models.DateTimeField('date joined', default=django.utils.timezone.now)
    # donor = models.ForeignKey(Donor, on_delete=models.CASCADE)

    def __str__(self):
        return self.id