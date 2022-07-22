#import path from django.urls
#import views fom . app folder
#create url  pattern

from django.urls import path
from . import views

urlpatterns = [

    path (" ", views.index, name='index'),
]