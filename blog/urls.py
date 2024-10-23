from django.urls import path
from . import views

#Hier wird views.index geladen
app_name =  'blog'
urlpatterns = [
    path('',  views.index, name='index'),
]