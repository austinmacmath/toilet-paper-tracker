from django.contrib import admin

# Register your models here.
from .models import Donor, Recipient
admin.site.register(Donor)
admin.site.register(Recipient)