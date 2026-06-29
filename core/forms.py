from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        # Explicitly exclude 'owner' to keep it secure from front-end manipulation
        fields = ['title', 'description', 'technologies_used', 'project_url', 'repository_url']
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., E-Commerce Platform'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Describe the architecture, milestones, and features...'}),
            'technologies_used': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Python, Django, PostgreSQL, Bootstrap'}),
            'project_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://...'}),
            'repository_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://github.com/...'}),
        }