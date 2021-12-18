from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist
from .forms import RegistroFormulario, UsuarioLoginFormulario
# Create your views here.

def home(request):
    post_list= Post.objects.all().order_by('created_on')
    context = {
        'posts': post_list,
    }
    return render(request, 'app/home.html', {} )



def post(request):
    return render(request, 'app/post.html' )
    
def loginView(request):
	titulo = 'login'
	form = UsuarioLoginFormulario(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		usuario = authenticate(username=username, password=password)
		login(request, usuario)
		return redirect('home')

	context = {
		'form':form,
		'titulo':titulo
	}

	return render(request, 'app/login.html', context)

def register(request):
	titulo = 'register'
	form = UsuarioLoginFormulario(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		usuario = authenticate(username=username, password=password)
		login(request, usuario)
		return redirect('home')

	context = {
		'form':form,
		'titulo':titulo
	}

	return render(request, 'app/register.html', context)

def logout_vista(request):
	logout(request)
	return redirect('/')
