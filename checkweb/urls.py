from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gioi-thieu', views.about, name='about'),
    path('lien-he', views.contact, name='contact'),
    path('check/', views.check, name='check'),
]
