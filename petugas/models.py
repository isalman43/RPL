from django.db import models

# Create your models here.

class tabelPetugas(models.Model) :
    kodePetugas = models.AutoField(primary_key=True)
    nama        = models.CharField(max_length=50)
    jabatan     = models.CharField(max_length=20)
    username    = models.CharField(max_length=20, unique=True)
    password    = models.CharField(max_length=35)

    def __str__(self):
        return f"{str(self.kodePetugas)} - {str(self.nama)}"