from django.contrib import admin
from .models import package, signupcred, logincred
# Register your models here.

admin.site.register(package)
admin.site.register(signupcred)
admin.site.register(logincred)