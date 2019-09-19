from django.urls import path
from . import views




app_name = 'articles'
# /articles/ _____

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_pk>/', views.detail, name='detail'),

    
    # path('new/',views.new, name='new'), 
    path('create/', views.create, name='create'),
    # /article/4/delete/
    path('<int:article_pk>/delete/', views.delete, name='delete'),
    
]
