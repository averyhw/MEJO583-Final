from django.contrib import admin
from . import models
from . models import Company

admin.site.register(models.Company)
