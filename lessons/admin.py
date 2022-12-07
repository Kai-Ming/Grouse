"""Configuration of the admin interface for lessons."""
from django.contrib import admin
from .models import User, Lesson, Invoice, Transfer


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


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
   """Configuration of the admin interface for invoices."""

   list_display = [
   'invoice_no', 'due_amount', 'due_date', 'created_at', 'updated_at'
   ]


@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
   """Configuration of the admin interface for transfers."""

   list_display = [
   'invoice_number', 'amount', 'date'
   ]
