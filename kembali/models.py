from django.db import models

from pinjam.models import tabelPinjamS, tabelPinjamN
from petugas.models import tabelPetugas

# Create your models here.

class tabelKembaliS(models.Model) :
    noKembaliS      = models.AutoField(primary_key=True)
    noPinjamS       = models.OneToOneField(tabelPinjamS, on_delete=models.CASCADE)
    tglKembali      = models.DateField()
    tglPengembalian = models.DateField()
    kodePetugas     = models.ForeignKey(tabelPetugas, on_delete=models.SET_NULL, null=True)
    denda           = models.IntegerField()

    def __str__(self):
        return str(self.noKembaliS)
    
class tabelKembaliN(models.Model) :
    noKembaliN      = models.AutoField(primary_key=True)
    noPinjamN       = models.OneToOneField(tabelPinjamN, on_delete=models.CASCADE)
    tglKembali      = models.DateField()
    tglPengembalian = models.DateField()
    kodePetugas     = models.ForeignKey(tabelPetugas, on_delete=models.SET_NULL, null=True)
    denda           = models.IntegerField()

    def __str__(self):
        return str(self.noKembaliN)