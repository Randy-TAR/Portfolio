from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from core.models import Project
from .forms import ProfileUpdateForm


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Magically saves the user to PostgreSQL with an encrypted password
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account successfully created for {username}! You can now login.')
            return redirect('login')  # We will build this login route soon!
    else:
        form = UserCreationForm()
        
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user() # Grabs the validated user object from the database
            auth_login(request, user) # Creates a secure session cookie in the browser
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('dashboard') # Temporary redirect until we build the dashboard!
    else:
        form = AuthenticationForm()
        
    return render(request, 'accounts/login.html', {'form': form})

# Add this brand new view function at the bottom:
def logout_view(request):
    auth_logout(request) # Clears session tracking variables instantly
    messages.info(request, "You have been successfully logged out.")
    return redirect('login') # Sends the user back to the login page cleanly


@login_required
def dashboard_view(request):
    # 2. Fetch all projects belonging exclusively to the logged-in user
    user_projects = request.user.projects.all() 
    
    # 3. Pass the projects data to the template using the context dictionary
    context = {
        'projects': user_projects
    }
    return render(request, 'accounts/dashboard.html', context)

@login_required
def profile_view(request):
    # Fetch the profile instance belonging exclusively to the logged-in user
    profile = request.user.profile 
    
    if request.method == 'POST':
        # Pass request.FILES to safely handle image streams coming from the browser
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your professional profile has been updated successfully!")
            return redirect('profile')
    else:
        # Pre-populate the form inputs with the data currently stored in PostgreSQL
        form = ProfileUpdateForm(instance=profile)
        
    return render(request, 'accounts/profile.html', {'form': form})

