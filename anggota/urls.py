
from django.urls import path

from . import views

urlpatterns = [
    path('siswa/', views.index),
    path('siswa/tambah/', views.tambah),
    path('siswa/<int:no_siswa>/update/', views.update),
    path('siswa/<int:no_siswa>/hapus/', views.hapus),

    path('non/', views.indexNon),
    path('non/tambah/', views.tambahNon),
    path('non/<int:non>/update/', views.updateNon),
    path('non/<int:non>/hapus/', views.hapusNon),
    
]
