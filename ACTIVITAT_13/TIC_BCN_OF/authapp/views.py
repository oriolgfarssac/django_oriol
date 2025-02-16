from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import Usuari

# Login sense sessió
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    error_message = None

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                usuari = Usuari.objects.get(email=email)
                if usuari.contrasenya == password:  # Comprovació simple (NO segura)
                    return render(request, 'home.html', {'usuari': usuari})  # Redirigeix a home
                else:
                    error_message = "Contrasenya incorrecta"
            except Usuari.DoesNotExist:
                error_message = "Usuari no existent"

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form, 'error': error_message})



# Login amb sessió
def login_view_sessio(request):
    form = LoginForm()
    error_message = ""

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            usuari = Usuari.objects.filter(email=email).first()

            if usuari:
                request.session['user_id'] = usuari.id
                return redirect('inici')
            else:
                error_message = "Credencials incorrectes."

    return render(request, 'login.html', {"form": form, "error": error_message})


# Logout
def logout_view(request):
    request.session.flush()
    return redirect('login')


# Pàgina d'inici
def inici_view(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')

    usuari = Usuari.objects.get(id=user_id)
    return render(request, 'inici.html', {"usuari": usuari})
