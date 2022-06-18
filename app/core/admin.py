from django.contrib import admin

# Register your models here.

from .models import Sample,SampleTwo

admin.site.register(Sample)
admin.site.register(SampleTwo)