from django.urls import path

from . import views

app_name = 'lr'
urlpatterns = [ 
    path('', views.index, name = 'index'),
    path('terms/', views.terms, name = 'terms'),
    path('add-review/', views.add_review, name = 'add-review'),
    path('add-review/post/', views.add_review_post, name = 'add-review-post'),
    path('add-review/added/', views.review_added, name = 'review-added')
]