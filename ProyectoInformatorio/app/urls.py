from django.urls import path
from.views import home, logueo, post , nuevologin

urlpatterns = [
    path('', home, name="home"),
    path('logueo/', logueo, name="logueo"),
    path('post/', post, name="post"),
    path('nuevologin/', nuevologin, name="nuevologin"),

]