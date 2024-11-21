# middleware.py
from django.shortcuts import redirect

class PreventGoogleAuthBackNavigationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the request is for the Google callback URL
        if 'accounts/google/login/callback/' in request.path and request.user.is_authenticated:
            return redirect('/api/tasks/')  # Or your desired redirect URL

        response = self.get_response(request)
        
        # Add headers to prevent browser back button caching
        response['Cache-Control'] = 'no-cache, no-store, must-revalidate, private'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'
        
        return response