from django.db import models
from anggota.models import tabelNon, tabelSiswa
from petugas.models import tabelPetugas
from buku.models import tabelBuku

# Create your models here.

class tabelPinjamS(models.Model) :
    noPinjamS       = models.AutoField(primary_key=True)

    tglPinjam       = models.DateField()
    tglKembali      = models.DateField()

    no_anggota      = models.ForeignKey(tabelSiswa, on_delete=models.SET_NULL, null=True)
    kodePetugas     = models.ForeignKey(tabelPetugas, on_delete=models.SET_NULL, null=True)
    kodebuku        = models.ForeignKey(tabelBuku, on_delete=models.SET_NULL, null=True)

    jumlah          = models.IntegerField()

class tabelPinjamN(models.Model) :
    noPinjamN       = models.AutoField(primary_key=True)

    tglPinjam       = models.DateField()
    tglKembali      = models.DateField()

    no_anggotaN     = models.ForeignKey(tabelNon, on_delete=models.SET_NULL, null=True)
    kodePetugas     = models.ForeignKey(tabelPetugas, on_delete=models.SET_NULL, null=True)
    kodebuku        = models.ForeignKey(tabelBuku, on_delete=models.SET_NULL, null=True)
    
    jumlah          = models.IntegerField()
