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
    
    path('<int:article_pk>/update/', views.update, name='update'),
    # /article/3/comments/
    path('<int:article_pk>/comments',views.comments_create, name='comments_create')
]
