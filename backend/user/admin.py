from django.contrib import admin
from . import models
from django.contrib.auth.models import Group
from .models import CustomUser, Booking


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'created_at', 'updated_at', 'is_staff', 'is_active')
    search_fields = ('username', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class BookingAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'phone_number', 'choice', 'date_created')
    search_fields = ('first_name', 'choice')
    filter_horizontal = ()


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.unregister(Group)