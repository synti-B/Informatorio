from django.urls import path
from.views import home, loginView, logout_vista, post , registro

urlpatterns = [
    path('', home, name="home"),
    path('logout_vista/', logout_vista, name="logout_vista"),
    path('post/', post, name="post"),
    path('login/', loginView, name="login"),
     path('registro/', registro, name="registro"),

]