from django.db import models

# Create your models here.

class tabelBuku(models.Model) :
    kodebuku     = models.AutoField(primary_key=True)
    judul        = models.CharField(max_length=50)
    penerbit     = models.CharField(max_length=50)
    pengarang    = models.CharField(max_length=50)
    thnterbit    = models.CharField(max_length=4)
    kotaterbit   = models.CharField(max_length=20)
    bahasa       = models.CharField(max_length=20)
    edisi        = models.CharField(max_length=20)
    deskripsi    = models.CharField(max_length=50)

    def __str__(self):
        return f"{str(self.kodebuku)} - {str(self.judul)}"