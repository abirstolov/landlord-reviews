from django.urls import path

from . import views

app_name = 'lr'
urlpatterns = [ 
    path('', views.index, name = 'index'),
    path('terms/', views.terms, name = 'terms'),
    path('add-review/', views.add_review, name = 'add-review')
]