from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

def authentication(request):
    if 'next' in request.GET:
        request.session['next'] = request.GET['next']
    return render(request, 'authentication/authentication.html')


def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            next_url = request.session.get('next', '/home')
            if 'next' in request.GET:
                del request.session['next']  # Supprimez le 'next' de la session après utilisation
            return redirect(next_url)
        
        else: 
            messages.error(request, "Identifiants invalides.", extra_tags='login_error')
    if 'next' in request.GET:
        request.session['next'] = request.GET['next']
    return render(request, 'authentication/authentication.html')

def logout_user(request):
    
    logout(request)
    return redirect('/')
