from django.contrib import admin
from .models import Inquiry

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    # Columns to show in the admin dashboard list view grid
    list_display = ('subject', 'sender_name', 'sender_email', 'category', 'created_at', 'is_resolved')
    
    # Sidebar filtering panels
    list_filter = ('category', 'is_resolved', 'created_at')
    
    # Search constraints indexing
    search_fields = ('sender_name', 'sender_email', 'subject', 'message')
    
    # Allows editing the resolution status directly from the grid view row
    list_editable = ('is_resolved',)