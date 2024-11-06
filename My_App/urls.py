from django.urls import  path
from My_App import  views
urlpatterns =[
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]