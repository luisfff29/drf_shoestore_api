from django.contrib import admin
from shoe_store import models


# Register your models here.
admin.site.register(models.Manufacturer)
admin.site.register(models.ShoeType)
admin.site.register(models.ShoeColor)
admin.site.register(models.Shoe)
