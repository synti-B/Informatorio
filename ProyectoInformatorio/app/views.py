from django.shortcuts import render, redirect, get_object_or_404,reverse
from .models import Post
from django.contrib.auth import authenticate, login, logout
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

def registro(request):

	titulo = 'Crear una Cuenta'
	if request.method == 'POST':
		form = RegistroFormulario(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form = RegistroFormulario()

	context = {

		'form':form,
		'titulo': titulo

	}

	return render(request, 'registro.html', context)


def logout_vista(request):
	logout(request)
	return redirect('/')
