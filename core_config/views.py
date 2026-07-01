from django.shortcuts import render

def custom_page_not_found_view(request, exception):
    # System intercepts 404 routes and serves our branded template
    return render(request, 'errors/404.html', status=404)

def custom_permission_denied_view(request, exception=None):
    # System intercepts unauthorized actions and serves our safety warning template
    return render(request, 'errors/403.html', status=403)