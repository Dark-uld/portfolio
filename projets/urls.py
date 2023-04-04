from django.urls import path
from . import views


urlpatterns = [
    path('', views.getIndex, name="index"),
    path('login/', views.loginPage, name="login"),
    path('contact/', views.createMessage, name="contact"),
    path('messages/', views.getMessages, name="tout_messages"),
    
]