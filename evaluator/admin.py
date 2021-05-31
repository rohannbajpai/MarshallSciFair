from django.contrib import admin
from .models import projects, event, schedule

# Register your models here.
admin.site.register(projects)
admin.site.register(event)
admin.site.register(schedule)