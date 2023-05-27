
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('tambah/', views.tambah),
    path('<int:no_anggota>/update/', views.update, name='update_anggota'),
    path('<int:no_anggota>/hapus/', views.hapus),
]
