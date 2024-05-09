from django.urls import path
from . import views

# route, view, name 
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'), #Use this login/ path for another page.
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
]