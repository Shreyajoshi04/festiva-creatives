from django.contrib import admin
from .models import EventCategory, EventTheme, Feedback

admin.site.register(EventCategory)
admin.site.register(EventTheme)
admin.site.register(Feedback)

# Register your models here.
