from django import forms
from .models import Inquiry

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        # Exclude 'is_resolved' so public visitors can't mark their own tickets as solved!
        fields = ['sender_name', 'sender_email', 'subject', 'category', 'message']
        
        # Injecting Bootstrap classes directly into the form rendering loop
        widgets = {
            'sender_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Full Name'}),
            'sender_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'What is this regarding?'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Type your proposal or support request detail...'}),
        }