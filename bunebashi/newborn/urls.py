from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='main'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('home/', views.home, name='home'),
    path('services/', views.sservices, name='services'),
    path('profile/<str:userid>/', views.profile, name='profile'),
   # path('register/', views.register, name='register'),
    #path('login/', views.login_view, name='login'),
    #path('profile/<str:userid>/my_services', views.myservices, name='myservices')
]