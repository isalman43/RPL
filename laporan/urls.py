from django.urls import path

from . import views

urlpatterns = [
    path('siswa/', views.siswa),
    path('non/', views.non),
    path('petugas/', views.petugas),
    path('buku/', views.buku),
    # path('pinjam/', views.pinjam),
    # path('kembali/', views.kembali),
]
