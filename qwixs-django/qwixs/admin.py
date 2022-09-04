from django.contrib import admin
from .models import Owner, Business, Services


# Register your models here.

admin.site.register(Owner)
admin.site.register(Business)
admin.site.register(Services)
