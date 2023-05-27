from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('tambah/', views.tambah),
    path('<int:petugas_id>/update/', views.update, name='update_petugas'),
    path('<int:petugas_id>/hapus/', views.hapus),
]
