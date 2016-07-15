from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponseRedirect
from usuario.forms import CustomUserCreationForm
from django.contrib import auth
from django.utils import timezone

# Create your views here.
def home(request):
    # Se envia la variable posts
    return render(request, 'usuario/home.html')


def login(request):
    return render(request, 'usuario/login.html')


def register_user(request):

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register_success')  # page success

    else:
        form = CustomUserCreationForm()
    return render(request, 'usuario/register.html', {'form': form})

def register_success(request):
    return render(request, 'usuario/register_success.html')

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')


def loggedin(request):
    return render(request, 'usuario/loggedin.html',{'user': request.user })

def invalid_login(request):
    return render(request, 'usuario/invalid_login.html')

def logout(request):
    auth.logout(request)
    return render(request, 'usuario/logout.html')
