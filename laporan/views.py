from django.shortcuts import render, redirect
from anggota.models import tabelSiswa,tabelNon
from petugas.models import tabelPetugas
from buku.models import tabelBuku
from pinjam.models import tabelPinjamS, tabelPinjamN
from kembali.models import tabelKembaliS, tabelKembaliN

# Create your views here.

def siswa(request) :

    if 'user_id' in request.session :

        tbSiswa = tabelSiswa.objects.all()

        # DICTIONARY, MENAMPUNG DATA
        dictionary = {
            'datasiswa'   : tbSiswa
        }

        return render(request, 'laporan/siswa.html', dictionary)
    
    else :
        return redirect('login/')

def non(request) :

    if 'user_id' in request.session :

        tbnon = tabelNon.objects.all()

        # DICTIONARY, MENAMPUNG DATA
        dictionary = {
            'datanon'   : tbnon
        }

        return render(request, 'laporan/non.html', dictionary)
    
    else :
        return redirect('login/')

def petugas(request) :

    if 'user_id' in request.session :

        tbpetugas = tabelPetugas.objects.all()

        # DICTIONARY, MENAMPUNG DATA
        dictionary = {
            'datapetugas'   : tbpetugas
        }

        return render(request, 'laporan/petugas.html', dictionary)
    
    else :
        return redirect('login/')

def buku(request) :

    if 'user_id' in request.session :

        tbbuku = tabelBuku.objects.all()

        # DICTIONARY, MENAMPUNG DATA
        dictionary = {
            'databuku'   : tbbuku
        }

        return render(request, 'laporan/buku.html', dictionary)
    
    else :
        return redirect('login/')

def pinjam(request) :

    if 'user_id' in request.session :

        pinjamS = tabelPinjamS.objects.all()
        pinjamN = tabelPinjamN.objects.all()

        # DICTIONARY, MENAMPUNG DATA
        dictionary = {
            'dataPinjamS'   : pinjamS,
            'dataPinjamN'   : pinjamN,
        }

        return render(request, 'laporan/pinjam.html', dictionary)
    
    else :
        return redirect('login/')

def kembali(request) :

    if 'user_id' in request.session :

        tbkembaliS = tabelKembaliS.objects.all()
        tbkembaliN = tabelKembaliN.objects.all()

        # DICTIONARY, MENAMPUNG DATA
        dictionary = {
            'datakembaliS'   : tbkembaliS,
            'datakembaliN'   : tbkembaliN,
        }

        return render(request, 'laporan/kembali.html', dictionary)
    
    else :
        return redirect('login/')
