from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    # Relational link tying the project to its developer creator
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    
    # Core project identity tags
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    # Engineering metadata
    technologies_used = models.CharField(max_length=250, help_text="Separate tags with commas. e.g., Python, Django, PostgreSQL")
    project_url = models.URLField(max_length=200, blank=True, verbose_name="Live Deployment URL")
    repository_url = models.URLField(max_length=200, blank=True, verbose_name="Source Code Repository")
    
    # System chronological audit metrics
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at'] # Ensures the newest projects always display first

    def __str__(self):
        return self.title