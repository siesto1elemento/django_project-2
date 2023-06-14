# . means current directory
from . import views
from django.urls import path


urlpatterns = [
    path('hello/',views.index, name='index'),
    path('item/',views.item, name='item'),
    path('sauce/',views.sauce,name='sauce')
]