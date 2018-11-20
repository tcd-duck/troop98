from django.contrib import admin

# Register your models here.
from bwca.models import Camper, Outfitter

admin.site.register(Camper)

admin.site.register(Outfitter)