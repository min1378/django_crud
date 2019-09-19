from django.urls import path
from . import views





# /articles/ _____

urlpatterns = [
    path('', views.index),
    path('<int:article_pk>/', views.detail),


    path('new/',views.new),
    path('create/', views.create),
    # /article/4/delete/
    path('<int:article_pk>/delete/', views.delete),
    
]
