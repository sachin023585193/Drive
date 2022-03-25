from django.contrib import admin
from .models import Drive

class DriveAdmin(admin.ModelAdmin):
    list_display = ('name','size','uploaded','extension')
    search_fields = ('name',)
    ordering = ('-uploaded',)
# Register your models here.
admin.site.register(Drive,DriveAdmin)