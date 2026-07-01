from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import InquiryForm

def contact_view(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            # Cleanly save the valid data object right down into PostgreSQL
            inquiry = form.save()
            
            # Send feedback to the user based on the category they picked
            messages.success(
                request, 
                f"Thank you, {inquiry.sender_name}! Your message regarding '{inquiry.subject}' has been transmitted to our systems."
            )
            return redirect('contact')
    else:
        form = InquiryForm()
        
    return render(request, 'communications/contact.html', {'form': form})