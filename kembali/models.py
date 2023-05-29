from django.db import models

from pinjam.models import tabelPinjamS
from petugas.models import tabelPetugas

# Create your models here.

class tabelKembaliS(models.Model) :
    noKembaliS      = models.AutoField(primary_key=True)
    noPinjamS       = models.ForeignKey(tabelPinjamS, on_delete=models.CASCADE, null=True)
    tglKembali      = models.DateField()
    tglPengembalian = models.DateField()
    kodePetugas     = models.ForeignKey(tabelPetugas, on_delete=models.SET_NULL, null=True)
    denda           = models.IntegerField()

    def __str__(self):
        return str(self.noKembaliS)