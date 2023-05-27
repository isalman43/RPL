from django.shortcuts import render,redirect, get_object_or_404

from . models import anggotaSiswa
from. forms import formAnggotaSiswa
# Create your views here.

def index(request) :
    # MENGAMBIL SEMUA FIELDS(KOLOM) TABEL PETUGAS
    tbAnggota = anggotaSiswa.objects.all()

    # DICTIONARY, MENAMPUNG DATA
    dictionary = {
        'dataAnggota'   : tbAnggota
    }
    return render(request, 'anggota/index.html', dictionary)

def tambah(request) :

    # MENGAMBIL FORM PETUGAS
    form = formAnggotaSiswa()

    # DICTIONARY
    dictionary = {
        'dataForm'  : form
    }

    # TAMBAH DATA DARI FORM (HTML)
    if request.method == "POST":

        # MENGAMBIL DATA DARI FORM
        form = formAnggotaSiswa(request.POST)

        # VALIDASI FORM
        if form.is_valid():

            # MENGAMBIL INSTANCE/OBJEK DARI FORM TANPA DI SIMPAN (BISA DI EDIT)
            form.save()

            # KEMBALI KE HALAMAN PETUGAS
            return redirect('../')

    return render(request, 'anggota/tambah.html', dictionary)

def update(request, no_anggota) :

    anggotaS = get_object_or_404(anggotaSiswa, no_anggota=no_anggota)

    if request.method == 'POST':
        form = formAnggotaSiswa(request.POST, instance=anggotaS)
        if form.is_valid():

            form.save()

            return redirect('../../')
    else:
        form = formAnggotaSiswa(instance=anggotaS)

    dictionary  = {
        'dataForm'      : form,
        'dataAnggota'   : anggotaS,
    }

    return render(request, 'anggota/update.html', dictionary)

def hapus(request, no_anggota):

    anggotaS = get_object_or_404(anggotaSiswa, no_anggota=no_anggota)

    if anggotaS.delete() :
        return redirect('../../')
    else:
        dictionary = {
            'error_message': 'Data tidak dihapus.'
        }

    return render(request, 'anggota/index.html', dictionary)
