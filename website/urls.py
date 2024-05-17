from django.urls import path
from . import views

# route, view, name 
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'), #Use this login/ path for another page.
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:primary_key>', views.customer_record, name='record'),
    path('delete_record/<int:primary_key>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:primary_key>', views.update_record, name='update_record'),
]