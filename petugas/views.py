import hashlib
from django.shortcuts import render, redirect, get_object_or_404

from . models import tabelPetugas
from . forms import formPetugas

# Create your views here.

def index(request) :

    # MENGAMBIL SEMUA FIELDS(KOLOM) TABEL PETUGAS
    tbPetugas = tabelPetugas.objects.all()

    # DICTIONARY, MENAMPUNG DATA
    dictionary = {
        'dataPetugas'   : tbPetugas
    }

    return render(request, 'petugas/index.html', dictionary)

def tambah(request) :

    # MENGAMBIL FORM PETUGAS
    form = formPetugas()

    # DICTIONARY
    dictionary = {
        'dataForm'  : form
    }

    # TAMBAH DATA DARI FORM (HTML)
    if request.method == "POST":

        # MENGAMBIL DATA DARI FORM
        form = formPetugas(request.POST)

        # VALIDASI FORM
        if form.is_valid():

            # MENGAMBIL INSTANCE/OBJEK DARI FORM TANPA DI SIMPAN (BISA DI EDIT)
            petugas = form.save(commit=False)

            # AMBIL DATA PASSWORD
            password = request.POST.get('password')
            # ENSKRIPSI PASSWORD
            hashed_password = hashlib.md5(password.encode()).hexdigest()
            # MENGEMBALIKAN DATA PASSWORD
            petugas.password = hashed_password

            # SMPAN PASSWORD
            petugas.save()

            # KEMBALI KE HALAMAN PETUGAS
            return redirect('../')

    return render(request, 'petugas/tambah.html', dictionary)

def update(request, petugas_id) :

    petugas = get_object_or_404(tabelPetugas, kodePetugas=petugas_id)

    if request.method == 'POST':
        form = formPetugas(request.POST, instance=petugas)
        if form.is_valid():

            # MENGAMBIL INSTANCE/OBJEK DARI FORM TANPA DI SIMPAN (BISA DI EDIT)
            petugas = form.save(commit=False)

            # AMBIL DATA PASSWORD
            password = request.POST.get('password')
            # ENSKRIPSI PASSWORD
            hashed_password = hashlib.md5(password.encode()).hexdigest()
            # MENGEMBALIKAN DATA PASSWORD
            petugas.password = hashed_password

            # SMPAN PASSWORD
            petugas.save()

            return redirect('../../')
    else:
        form = formPetugas(instance=petugas)

    dictionary  = {
        'dataForm'      : form,
        'dataPetugas'   : petugas,
    }

    return render(request, 'petugas/update.html', dictionary)

def hapus(request, petugas_id):

    petugas = get_object_or_404(tabelPetugas, kodePetugas=petugas_id)

    if petugas.delete() :
        return redirect('../../')
    else:
        dictionary = {
            'error_message': 'Data tidak dihapus.'
        }

    return render(request, 'petugas/index.html', dictionary)
