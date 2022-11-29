"""Configuration of the admin interface for lessons."""
from django.contrib import admin
from .models import User, Lesson


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
   """Configuration of the admin interface for users."""

   list_display = [
   'username', 'first_name', 'last_name', 'email', 'user_type', 'is_active',
   ]

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
   """Configuration of the admin interface for lessons."""

   list_display = [
   'student', 'teacher', 'number_of_lessons', 'lesson_duration', 'price', 'fulfilled', 'paid_type',
   ]