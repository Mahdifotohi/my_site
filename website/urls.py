from django.urls import path, include
from . import views


app_name = 'website'

urlpatterns = [
    path('',views.index_view,name='index'),
    path('about/',views.about_view,name='about'),
    path('contact/', views.content_view,name='contact'),
    path('elements/', views.elements_view,name='elements'),
]