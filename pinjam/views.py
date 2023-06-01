
from django.shortcuts import render, redirect, get_object_or_404

from . models import tabelPinjamS, tabelPinjamN
from . forms import formPinjamS, formPinjamN

# Create your views here.

def index(request) :

    if 'user_id' in request.session :

        pinjamSiswa = tabelPinjamS.objects.all()

        # DICTIONARY, MENAMPUNG DATA
        dictionary = {
            'dataPinjamS'   : pinjamSiswa
        }

        return render(request, 'pinjam/siswa/index.html', dictionary)
    
    else :
        return redirect('login/')

def tambah(request) :

    if 'user_id' in request.session :

        form = formPinjamS()

        # DICTIONARY
        dictionary = {
            'dataForm'  : form
        }

        # TAMBAH DATA DARI FORM (HTML)
        if request.method == "POST":

            # MENGAMBIL DATA DARI FORM
            form = formPinjamS(request.POST)

            # VALIDASI FORM
            if form.is_valid():

                pinjamS = form.save(commit=False)
                
                # Set the foreign key values
                pinjamS.no_anggota = form.cleaned_data['no_anggota']
                pinjamS.kodePetugas = form.cleaned_data['kodePetugas']
                pinjamS.kodebuku = form.cleaned_data['kodebuku']

                # Save the form
                pinjamS.save()

                return redirect('../')

        return render(request, 'pinjam/siswa/tambah.html', dictionary)
    
    else :
        return redirect('login/')

def update(request, id_pinjam) :

    if 'user_id' in request.session :

        instancePinjamS = get_object_or_404(tabelPinjamS, noPinjamS=id_pinjam)

        if request.method == 'POST':
            form = formPinjamS(request.POST, instance=instancePinjamS)
            if form.is_valid():

                pinjamS = form.save(commit=False)
                
                # Set the foreign key values
                pinjamS.no_anggota  = form.cleaned_data['no_anggota']
                pinjamS.kodePetugas = form.cleaned_data['kodePetugas']
                pinjamS.kodebuku    = form.cleaned_data['kodebuku']

                # Save the form
                pinjamS.save()

                return redirect('../../')
        else:
            form =formPinjamS(instance=instancePinjamS)

        dictionary  = {
            'dataForm'      : form,
            'dataPinjamS'      : instancePinjamS,
        }

        return render(request, 'pinjam/siswa/update.html', dictionary)
    
    else :
        return redirect('login/')

def hapus(request, id_pinjam):

    if 'user_id' in request.session :

        instancePinjamS = get_object_or_404(tabelPinjamS, noPinjamS=id_pinjam)

        if instancePinjamS.delete() :
            return redirect('../../')
        else:
            dictionary = {
                'error_message': 'Data tidak dihapus.'
            }

        return render(request, 'pinjam/siswa/index.html', dictionary)
    
    else :
        return redirect('login/')

def indexN(request) :

    if 'user_id' in request.session :

        pinjamNon = tabelPinjamN.objects.all()

        # DICTIONARY, MENAMPUNG DATA
        dictionary = {
            'dataPinjamN'   : pinjamNon
        }

        return render(request, 'pinjam/non/index.html', dictionary)
    
    else :
        return redirect('login/')

def tambahN(request) :

    if 'user_id' in request.session :

        form = formPinjamN()

        # DICTIONARY
        dictionary = {
            'dataForm'  : form
        }

        # TAMBAH DATA DARI FORM (HTML)
        if request.method == "POST":

            # MENGAMBIL DATA DARI FORM
            form = formPinjamN(request.POST)

            # VALIDASI FORM
            if form.is_valid():

                pinjamN = form.save(commit=False)
                
                # Set the foreign key values
                pinjamN.no_anggotaN = form.cleaned_data['no_anggotaN']
                pinjamN.kodePetugas = form.cleaned_data['kodePetugas']
                pinjamN.kodebuku = form.cleaned_data['kodebuku']

                # Save the form
                pinjamN.save()

                return redirect('../')

        return render(request, 'pinjam/non/tambah.html', dictionary)
    
    else :
        return redirect('login/')

def updateN(request, id_pinjam) :

    if 'user_id' in request.session :

        instancePinjamN = get_object_or_404(tabelPinjamN, noPinjamN=id_pinjam)

        if request.method == 'POST':
            form = formPinjamN(request.POST, instance=instancePinjamN)
            if form.is_valid():

                pinjamN = form.save(commit=False)
                
                # Set the foreign key values
                pinjamN.no_anggotaN  = form.cleaned_data['no_anggotaN']
                pinjamN.kodePetugas = form.cleaned_data['kodePetugas']
                pinjamN.kodebuku    = form.cleaned_data['kodebuku']

                # Save the form
                pinjamN.save()

                return redirect('../../')
        else:
            form =formPinjamN(instance=instancePinjamN)

        dictionary  = {
            'dataForm'      : form,
            'dataPinjamN'   : instancePinjamN,
        }

        return render(request, 'pinjam/non/update.html', dictionary)
    
    else :
        return redirect('login/')

def hapusN(request, id_pinjam):

    if 'user_id' in request.session :

        instancePinjamN = get_object_or_404(tabelPinjamN, noPinjamN=id_pinjam)

        if instancePinjamN.delete() :
            return redirect('../../')
        else:
            dictionary = {
                'error_message': 'Data tidak dihapus.'
            }

        return render(request, 'pinjam/non/index.html', dictionary)

    else :
        return redirect('login/')
