from django.urls import path
from.views import home, loginView, logout_vista, post, register
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name="home"), 
    path('logout_vista/', logout_vista, name="logout_vista"),
    path('post/', post, name="post"),
    path('login/', loginView, name="login"),
    path('register/', register, name="register"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)