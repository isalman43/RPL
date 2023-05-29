from django.urls import path

from . import views

urlpatterns = [
    path('siswa/', views.index),
    path('siswa/tambah/', views.tambah),
]
