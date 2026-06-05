from django.db import models

# Create your models here.
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    massage = models.TextField()
    created_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"