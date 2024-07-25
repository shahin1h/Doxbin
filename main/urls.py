from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dox/<slug:slug>/', views.dox, name='dox'),
    path('new', views.new_dox, name='new'),
]
