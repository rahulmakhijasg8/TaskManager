from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def login_cancelled(request):
    return redirect('/api/tasks')

def login_error(request):
    return redirect('/api/tasks')
