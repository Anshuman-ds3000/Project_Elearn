from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Enroll

# Optionally, create a custom admin class
class EnrollAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'created_at', 'updated_at')  # Fields to display in the list view
    list_filter = ('user', 'course')  # Filter by user and course
    search_fields = ('user__username', 'course__title')  # Allow searching by username and course title
    ordering = ('-created_at',)  # Default ordering by creation time (most recent first)

# Register the Enroll model with the custom admin class
admin.site.register(Enroll, EnrollAdmin)
