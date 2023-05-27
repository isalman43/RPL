from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('tambah/', views.tambah),
    path('<int:kodebuku>/update/', views.update),
    path('<int:kodebuku>/hapus/', views.hapus),
]
