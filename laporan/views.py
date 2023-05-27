from django.shortcuts import render
from anggota.models import tabelSiswa,tabelNon
from petugas.models import tabelPetugas
from buku.models import tabelBuku
# from pinjam.models import tabelPinjam
# from kembali.models import tabelKembali
# Create your views here.
def siswa(request) :

    tbSiswa = tabelSiswa.objects.all()

    # DICTIONARY, MENAMPUNG DATA
    dictionary = {
        'datasiswa'   : tbSiswa
    }

    return render(request, 'laporan/siswa.html', dictionary)

def non(request) :

    tbnon = tabelNon.objects.all()

    # DICTIONARY, MENAMPUNG DATA
    dictionary = {
        'datanon'   : tbnon
    }

    return render(request, 'laporan/non.html', dictionary)

def petugas(request) :

    tbpetugas = tabelPetugas.objects.all()

    # DICTIONARY, MENAMPUNG DATA
    dictionary = {
        'datapetugas'   : tbpetugas
    }

    return render(request, 'laporan/petugas.html', dictionary)

def buku(request) :

    tbbuku = tabelBuku.objects.all()

    # DICTIONARY, MENAMPUNG DATA
    dictionary = {
        'databuku'   : tbbuku
    }

    return render(request, 'laporan/buku.html', dictionary)

# def pinjam(request) :

#     tbpinjam = tabelPinjam.objects.all()

#     # DICTIONARY, MENAMPUNG DATA
#     dictionary = {
#         'datapinjam'   : tbpinjam
#     }

#     return render(request, 'laporan/pinjam.html', dictionary)

# def kembali(request) :

#     tbkembali = tabelKembali.objects.all()

#     # DICTIONARY, MENAMPUNG DATA
#     dictionary = {
#         'datakembali'   : tbkembali
#     }

#     return render(request, 'laporan/kembali.html', dictionary) 
