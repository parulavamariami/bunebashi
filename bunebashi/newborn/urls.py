from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='main'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('home/', views.home, name='home'),
    path('services/', views.sservices, name='services'),
    path('profile/<str:userid>/', views.profile, name='profile'),
    path('saving_rel/<str:userid>/', views.saving, name='saving'),
    path('remove_rel/<str:userid>/', views.remove, name='remove_service'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.register_user, name='signup'),

]
""" path('profile/<str:userid>/my_services', views.myservices, name='myservices')
    path('add/', views.add_book, name='add'),
    path('reading/<str:id>', views.reading, name='reading'),
    path('delete_book/<str:id>', views.delete_book, name='delete'),
    path('update_user/', views.update_user, name='update_user'),
    path('delete_comment/<str:id>', views.delete_comment, name='delete_comment')"""
