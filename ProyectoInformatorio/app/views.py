from django.shortcuts import render
from .models import Post

# Create your views here.

def home(request):
    post_list= Post.objects.all().order_by('created_on')
    context = {
        'posts': post_list,
    }
    return render(request, 'app/home.html', {} )

def logueo(request):
    return render(request, 'app/logueo.html')

def post(request):
    return render(request, 'app/post.html' )
    
def nuevologin(request):
    return render(request, 'app/nuevologin.html')