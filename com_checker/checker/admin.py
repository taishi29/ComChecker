from django.contrib import admin
# Register your models here.
from django.contrib import admin
from .models import Company, CompanyImage

admin.site.register(Company)
admin.site.register(CompanyImage)
