from django.db import models  # <-- CORE FIX: Change 'import db' to 'import models'
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    
    # TYPO FIX ALSO: Changed 'upload_url' to 'upload_to' (Django's correct parameter name)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='profile_pics/default.png')
    
    phone_number = models.CharField(max_length=20, blank=True)
    github_link = models.URLField(max_length=200, blank=True)
    linkedin_link = models.URLField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Professional Profile Layout"