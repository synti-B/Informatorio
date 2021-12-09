from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    return render(request, 'app/home.html', {} )

def logueo(request):
    return render(request, 'app/logueo.html')

def post(request):
    return render(request, 'app/post.html' )
    
def nuevologin(request):
    return render(request, 'app/nuevologin.html')