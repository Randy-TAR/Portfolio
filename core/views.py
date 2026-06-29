from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from .models import Project
from .forms import ProjectForm

@login_required
def project_create_view(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            # 1. Pause saving to the database so we can modify the object
            project = form.save(commit=False)
            
            # 2. Securely bind the logged-in user as the owner
            project.owner = request.user
            
            # 3. Save the complete object permanently to PostgreSQL
            project.save()
            
            messages.success(request, f"Project '{project.title}' has been successfully created!")
            return redirect('dashboard')
    else:
        form = ProjectForm()
        
    return render(request, 'core/project_form.html', {'form': form})

@login_required
def project_update_view(request, pk):
    # 1. Safely fetch the specific project instance or throw a clean 404 screen
    project = get_object_or_404(Project, pk=pk)
    
    # 2. SECURITY GUARD: Confirm the logged-in user actually owns this record
    if project.owner != request.user:
        raise PermissionDenied  # Throws a standard HTTP 403 Forbidden Error
        
    if request.method == 'POST':
        # Pass the existing 'project' instance so Django updates it instead of creating a new row
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, f"Project '{project.title}' updated successfully!")
            return redirect('dashboard')
    else:
        form = ProjectForm(instance=project)
        
    context = {
        'form': form,
        'project': project,
        'is_edit': True # Flag to reuse our form template dynamically
    }
    return render(request, 'core/project_form.html', context)

@login_required
def project_delete_view(request, pk):
    # 1. Fetch the project or return a clean 404 error
    project = get_object_or_404(Project, pk=pk)
    
    # 2. SECURITY GUARD: Ensure only the creator can destroy this record
    if project.owner != request.user:
        raise PermissionDenied
        
    if request.method == 'POST':
        # 3. User confirmed the action; permanently drop the row from PostgreSQL
        project.delete()
        messages.warning(request, f"Project '{project.title}' has been permanently deleted.")
        return redirect('dashboard')
        
    # If it's a GET request, serve the confirmation warning template
    return render(request, 'core/project_confirm_delete.html', {'project': project})


def explorer_view(request):
    # 2. Capture the 'search' parameter value from the browser URL address bar
    search_query = request.GET.get('search', '')
    
    # Start with our base optimized global QuerySet JOIN layout
    projects = Project.objects.select_related('owner').all()
    
    # 3. If a user actually typed something in the search box, filter the database rows
    if search_query:
        projects = projects.filter(
            Q(title__icontains=search_query) | 
            Q(description__icontains=search_query) |
            Q(technologies_used__icontains=search_query)
        )
        
    context = {
        'projects': projects,
        'search_query': search_query # Pass it back to keep the text inside the input box!
    }
    return render(request, 'core/explorer.html', context)

