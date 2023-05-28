from django.db import models

# Create your models here.

class tabelSiswa(models.Model):
    no_anggota      = models.AutoField(primary_key=True)
    nis             = models.CharField(max_length=15)
    nama            = models.CharField(max_length=50)
    jurusan         = models.CharField(max_length=20)
    tanggal_lahir   = models.DateField()
    alamat          = models.CharField(max_length=50)
    kode_post       = models.CharField(max_length=20)
    hp              = models.CharField(max_length=20)

    def __str__(self):
        return f"{str(self.no_anggota)} - {str(self.nama)}"
    
class tabelNon(models.Model):
    no_anggotaN     = models.AutoField(primary_key=True)
    nip             = models.CharField(max_length=15)
    nama            = models.CharField(max_length=50)
    jabatan         = models.CharField(max_length=20)
    tanggal_lahir   = models.DateField()
    alamat          = models.CharField(max_length=50)
    kode_post       = models.CharField(max_length=20)
    hp              = models.CharField(max_length=20)

    def __str__(self):
        return f"{str(self.no_anggotaN)} - {str(self.nama)}"