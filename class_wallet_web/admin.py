from django.contrib import admin
from . import models

@admin.register(models.Part)
class PartAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    pass