from django.urls import path
from . import views

#Hier wird views.index geladen
app_name =  'web'
urlpatterns = [
    path('',  views.index, name='index'),
    path('register/', views.register, name='register')
]