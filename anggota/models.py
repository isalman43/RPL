from django.db import models

# Create your models here.

class anggotaSiswa(models.Model):
    no_anggota      = models.AutoField(primary_key=True)
    nim             = models.CharField(max_length=15)
    nama            = models.CharField(max_length=50)
    jurusan         = models.CharField(max_length=20)
    tanggal_lahir   = models.DateField()
    alamat          = models.CharField(max_length=50)
    kode_post       = models.CharField(max_length=20)
    hp              = models.CharField(max_length=20)
    
