
from django.shortcuts import render, redirect, get_object_or_404

from . models import tabelBuku
from . forms import formBuku

# Create your views here.

def index(request) :

    tbbuku = tabelBuku.objects.all()

    # DICTIONARY, MENAMPUNG DATA
    dictionary = {
        'databuku'   : tbbuku
    }

    return render(request, 'buku/index.html', dictionary)

def tambah(request) :

    form = formBuku()

    # DICTIONARY
    dictionary = {
        'dataForm'  : form
    }

    # TAMBAH DATA DARI FORM (HTML)
    if request.method == "POST":

        # MENGAMBIL DATA DARI FORM
        form = formBuku(request.POST)

        # VALIDASI FORM
        if form.is_valid():

            # MENGAMBIL INSTANCE/OBJEK DARI FORM TANPA DI SIMPAN (BISA DI EDIT)
            form.save()

            return redirect('../')

    return render(request, 'buku/tambah.html', dictionary)

def update(request, kodebuku) :

    instance_buku = get_object_or_404(tabelBuku, kodebuku=kodebuku)

    if request.method == 'POST':
        form = formBuku(request.POST, instance=instance_buku)
        if form.is_valid():

            # MENGAMBIL INSTANCE/OBJEK DARI FORM TANPA DI SIMPAN (BISA DI EDIT)
            form.save()

            return redirect('../../')
    else:
        form =formBuku(instance=instance_buku)

    dictionary  = {
        'dataForm'      : form,
        'databuku'      : instance_buku,
    }

    return render(request, 'buku/update.html', dictionary)

def hapus(request, kodebuku):

    instance_buku = get_object_or_404(tabelBuku, kodebuku=kodebuku)

    if instance_buku.delete() :
        return redirect('../../')
    else:
        dictionary = {
            'error_message': 'Data tidak dihapus.'
        }

    return render(request, 'buku/index.html', dictionary)
