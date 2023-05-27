from django.shortcuts import render,redirect, get_object_or_404

from . models import tabelSiswa, tabelNon
from. forms import formSiswa, formNon
# Create your views here.

def index(request) :
    if 'user id' in request.session :
        # MENGAMBIL SEMUA FIELDS(KOLOM) TABEL PETUGAS
        tbSiswa = tabelSiswa.objects.all()

        # DICTIONARY, MENAMPUNG DATA
        dictionary = {
            'dataSiswa'   : tbSiswa
        }
        return render(request, 'anggota/siswa/index.html', dictionary)
    else :
        return redirect('../../')

def tambah(request) :

    if 'user id' in request.session :
        # MENGAMBIL FORM PETUGAS
        form = formSiswa()

        # DICTIONARY
        dictionary = {
            'dataForm'  : form
        }

        # TAMBAH DATA DARI FORM (HTML)
        if request.method == "POST":

            # MENGAMBIL DATA DARI FORM
            form = formSiswa(request.POST)

            # VALIDASI FORM
            if form.is_valid():

                # MENGAMBIL INSTANCE/OBJEK DARI FORM TANPA DI SIMPAN (BISA DI EDIT)
                form.save()

                # KEMBALI KE HALAMAN PETUGAS
                return redirect('../')

        return render(request, 'anggota/siswa/tambah.html', dictionary)
    else :
        return redirect('../../../')

def update(request, no_siswa) :
    if 'user id' in request.session :
        instance_siswa = get_object_or_404(tabelSiswa, no_anggota=no_siswa)

        if request.method == 'POST':
            form = formSiswa(request.POST, instance=instance_siswa)
            if form.is_valid():

                form.save()

                return redirect('../../')
        else:
            form = formSiswa(instance=instance_siswa)

        dictionary  = {
            'dataForm'      : form,
            'dataSiswa'     : instance_siswa,
        }

        return render(request, 'anggota/siswa/update.html', dictionary)
    else :
        return redirect('../../../../')

def hapus(request, no_siswa):

    if 'user id' in request.session :
        instance_siswa = get_object_or_404(tabelSiswa, no_anggota=no_siswa)

        if instance_siswa.delete() :
            return redirect('../../')
        else:
            dictionary = {
                'error_message': 'Data tidak dihapus.'
            }

        return render(request, 'anggota/siswa/index.html', dictionary)
    else :
        return redirect('../../../../')
   
def indexNon(request) :
    if 'user id' in request.session :
           # MENGAMBIL SEMUA FIELDS(KOLOM) TABEL PETUGAS
        tbNon = tabelNon.objects.all()

        # DICTIONARY, MENAMPUNG DATA
        dictionary = {
            'dataNon'   : tbNon
        }
        return render(request, 'anggota/non/index.html', dictionary)
    else :
        return redirect('../../')
 
def tambahNon(request) :
    if 'user id' in request.session :
            # MENGAMBIL FORM PETUGAS
        form = formNon()

        # DICTIONARY
        dictionary = {
            'dataForm'  : form
        }

        # TAMBAH DATA DARI FORM (HTML)
        if request.method == "POST":

            # MENGAMBIL DATA DARI FORM
            form = formNon(request.POST)

            # VALIDASI FORM
            if form.is_valid():

                # MENGAMBIL INSTANCE/OBJEK DARI FORM TANPA DI SIMPAN (BISA DI EDIT)
                form.save()

                return redirect('../')

        return render(request, 'anggota/non/tambah.html', dictionary)
    else :
        return redirect('../../../')

def updateNon(request, non) :
    if 'user id' in request.session :
        instance_non = get_object_or_404(tabelNon, no_anggotaN=non)

        if request.method == 'POST':
            form = formNon(request.POST, instance=instance_non)
            if form.is_valid():

                form.save()

                return redirect('../../')
        else:
            form = formNon(instance=instance_non)

        dictionary  = {
            'dataForm'      : form,
            'dataNon'       : instance_non,
        }

        return render(request, 'anggota/non/update.html', dictionary)

    else :
        return redirect('../../../../')

def hapusNon(request, non):
    if 'user id' in request.session :
        instance_non = get_object_or_404(tabelNon, no_anggotaN=non)

        if instance_non.delete() :
            return redirect('../../')
        else:
            dictionary = {
                'error_message': 'Data tidak dihapus.'
            }

        return render(request, 'anggota/non/index.html', dictionary)
    else :
        return redirect('../../../../')

    
