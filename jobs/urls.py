from django.urls import path
from . import views




app_name = 'jobs'
# /jobs/ _____

urlpatterns = [
    path('', views.index, name='index'),
    path('past_jobs/', views.create, name='create'),

]