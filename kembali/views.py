from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from . models import tabelKembaliS
from . forms import formKembaliS

from pinjam.models import tabelPinjamS

def index(request) :

    tb = tabelKembaliS.objects.all()

    # DICTIONARY, MENAMPUNG DATA
    dictionary = {
        'dataKembaliS'   : tb
    }

    return render(request, 'kembali/siswa/index.html', dictionary)

def tambah(request) :



    if request.method == "POST" : 
        form    = formKembaliS(request.POST)

        # id_pinjam       = request.POST.get('noPinjamS')

        # instancePinjamS = get_object_or_404(tabelPinjamS, noPinjamS=id_pinjam)

        if form.is_valid() : 

            # form = formKembaliS(request.POST, instance=instancePinjamS)

            save = form.save(commit=False)

            formPinjam          = request.POST.get('noPinjamS')
            instancePinjam      = tabelPinjamS.objects.get(noPinjamS=formPinjam)
            tglKembali          = instancePinjam.tglKembali
            save.tglKembali     = tglKembali

            tglPengembalian = form.cleaned_data['tglPengembalian']
            selisih_hari = tglPengembalian - tglKembali

            if selisih_hari.days > 0:
                denda = selisih_hari.days * 500
            else:
                denda = 0

            save.denda = denda;

            
            # save.tglKembali     = form.cleaned_data['tglKembali']
            save.noPinjamS      = form.cleaned_data['noPinjamS']
            save.kodePetugas    = form.cleaned_data['kodePetugas']

            save.save()

            return redirect('../')
    
    else : 
        form = formKembaliS()

    # DICTIONARY, MENAMPUNG DATA
    dictionary = {
        'dataForm'   : form
    }

    return render(request, 'kembali/siswa/tambah.html', dictionary)

