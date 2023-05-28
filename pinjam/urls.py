from django.urls import path

from . import views

urlpatterns = [
    path('siswa/', views.index),
    path('siswa/tambah/', views.tambah),
    path('siswa/<int:id_pinjam>/update/', views.update),
    path('siswa/<int:id_pinjam>/hapus/', views.hapus),

    path('non/', views.indexN),
    path('non/tambah/', views.tambahN),
    path('non/<int:id_pinjam>/update/', views.updateN),
    path('non/<int:id_pinjam>/hapus/', views.hapusN),
]
