from django.db import models

# Create your models here.
class Donor(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField(default=0)
    latitude = models.DecimalField(max_digits=8, decimal_places=6)
    longitude = models.DecimalField(max_digits=8, decimal_places=6)
    points = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=200)
    join_date = models.DateTimeField('date joined')

    def __str__(self):
        return self.name

    def valid(self):
        return self.quantity > 0
class Recipient(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    request = models.IntegerField(default=1)
    latitude = models.DecimalField(max_digits=8, decimal_places=6)
    longitude = models.DecimalField(max_digits=8, decimal_places=6)
    join_date = models.DateTimeField('date joined')
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name