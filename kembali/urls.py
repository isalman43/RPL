from django.urls import path

from . import views

urlpatterns = [
    path('siswa/', views.index),
    path('siswa/tambah/', views.tambah),
    path('siswa/<int:id_kembali>/update/', views.update),
    path('siswa/<int:id_kembali>/hapus/', views.hapus),

    path('non/', views.indexN),
    path('non/tambah/', views.tambahN),
    path('non/<int:id_kembali>/update/', views.updateN),
    path('non/<int:id_kembali>/hapus/', views.hapusN),
]
