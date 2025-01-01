from django.contrib import admin
from .models import Student, Teacher

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """
    Custom admin interface for the Student model.

    list_display:
        Displays the student's full name, varsity ID, and email in the admin list view.
    search_fields:
        Allows searching by full name, varsity ID, and email in the admin interface.
    """
    list_display = ('full_name', 'varsity_id', 'email')  # Customize fields to display in the list view
    search_fields = ('full_name', 'varsity_id', 'email')  # Enable search functionality

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    """
    Custom admin interface for the Teacher model.

    list_display:
        Displays the teacher's full name and email in the admin list view.
    search_fields:
        Allows searching by full name and email in the admin interface.
    """
    list_display = ('full_name', 'email')  # Customize fields to display in the list view
    search_fields = ('full_name', 'email')  # Enable search functionality