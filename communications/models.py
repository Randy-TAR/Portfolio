from django.db import models

class Inquiry(models.Model):
    # Category Classification System
    INQUIRY_CHOICES = [
        ('GENERAL', 'General System Inquiry'),
        ('COLLAB', 'Technical Collaboration Proposal'),
        ('SUPPORT', 'Platform Bug/Support Ticket'),
    ]

    # Core Form Attributes
    sender_name = models.CharField(max_length=100)
    sender_email = models.EmailField()
    subject = models.CharField(max_length=200)
    category = models.CharField(max_length=10, choices=INQUIRY_CHOICES, default='GENERAL')
    message = models.TextField()
    
    # System Metadata Trackers
    created_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False) # Allows admins to mark tickets as completed

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Inquiries" # Fixes the plural spelling inside Django Admin

    def __str__(self):
        return f"[{self.get_category_display()}] - {self.subject} from {self.sender_name}"