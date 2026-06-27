from django import forms
from .models import Profile

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        # Exclude 'user' and 'created_at' so developers can't change their account ownership properties!
        fields = ['bio', 'profile_picture', 'phone_number', 'github_link', 'linkedin_link']
        
        # Adding Bootstrap styling hooks directly to the form elements
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Tell us about your engineering stack...'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+237...'}),
            'github_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://github.com/...'}),
            'linkedin_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://linkedin.com/in/...'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
        }

        