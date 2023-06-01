from django.shortcuts import render, redirect, get_object_or_404

from . models import tabelKembaliS, tabelKembaliN
from . forms import formKembaliS, formKembaliN

from pinjam.models import tabelPinjamS, tabelPinjamN

def index(request) :

    if 'user_id' in request.session :

        tb = tabelKembaliS.objects.all()

        # DICTIONARY, MENAMPUNG DATA
        dictionary = {
            'dataKembaliS'   : tb
        }

        return render(request, 'kembali/siswa/index.html', dictionary)
    
    else :
        return redirect('login/')

def tambah(request) :

    if 'user_id' in request.session :

        if request.method == "POST" : 
            form    = formKembaliS(request.POST)

            # id_pinjam       = request.POST.get('noPinjamS')

            # instancePinjamS = get_object_or_404(tabelPinjamS, noPinjamS=id_pinjam)

            if form.is_valid() : 

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
    
    else :
        return redirect('login/')

def update(request, id_kembali) :

    if 'user_id' in request.session :

        instanceKembaliS = get_object_or_404(tabelKembaliS, noKembaliS=id_kembali)

        if request.method == 'POST':
            form = formKembaliS(request.POST, instance=instanceKembaliS)
            if form.is_valid():

                save = form.save(commit=False)
                
                formPinjam          = request.POST.get('noPinjamS')
                instancePinjam      = tabelPinjamS.objects.get(noPinjamS=formPinjam)
                tglKembali          = instancePinjam.tglKembali
                save.tglKembali     = tglKembali

                tglPengembalian     = form.cleaned_data['tglPengembalian']
                selisih_hari        = tglPengembalian - tglKembali

                if selisih_hari.days > 0:
                    denda = selisih_hari.days * 500
                else:
                    denda = 0
                
                # Set the foreign key values
                save.denda = denda;

                save.noPinjamS      = form.cleaned_data['noPinjamS']
                save.kodePetugas    = form.cleaned_data['kodePetugas']

                # Save the form
                save.save()

                return redirect('../../')
        else:
            form =formKembaliS(instance=instanceKembaliS)
            form.fields['noPinjamS'].initial = instanceKembaliS.noPinjamS
            # form.fields['noPinjamS'].disable = True

        dictionary  = {
            'dataForm'      : form,
            # 'dataKembaliS'   : instanceKembaliS,
        }

        return render(request, 'kembali/siswa/update.html', dictionary)
    
    else :
        return redirect('login/')

def hapus(request, id_kembali):

    if 'user_id' in request.session :

        instanceKembaliS = get_object_or_404(tabelKembaliS, noKembaliS=id_kembali)

        if instanceKembaliS.delete() :
            return redirect('../../')
        else:
            dictionary = {
                'error_message': 'Data tidak dihapus.'
            }

        return render(request, 'kembali/siswa/index.html', dictionary)
    
    else :
        return redirect('login/')

def indexN(request) :

    if 'user_id' in request.session :

        tb = tabelKembaliN.objects.all()

        # DICTIONARY, MENAMPUNG DATA
        dictionary = {
            'dataKembaliN'   : tb
        }

        return render(request, 'kembali/non/index.html', dictionary)
    
    else :
        return redirect('login/')

def tambahN(request) :

    if 'user_id' in request.session :

        if request.method == "POST" : 
            form    = formKembaliN(request.POST)

            if form.is_valid() : 

                save = form.save(commit=False)

                # Mengambil No Pinjam dari Form
                formPinjam          = request.POST.get('noPinjamN')
                # Mengambil Instance di Tabel Pinjam
                instancePinjam      = tabelPinjamN.objects.get(noPinjamN=formPinjam)
                tglKembali          = instancePinjam.tglKembali
                save.tglKembali     = tglKembali

                tglPengembalian     = form.cleaned_data['tglPengembalian']
                selisih_hari        = tglPengembalian - tglKembali

                if selisih_hari.days > 0:
                    denda = selisih_hari.days * 500
                else:
                    denda = 0

                save.denda = denda;

                save.noPinjamN      = form.cleaned_data['noPinjamN']
                save.kodePetugas    = form.cleaned_data['kodePetugas']

                save.save()

                return redirect('../')
        
        else : 
            form = formKembaliN()

        # DICTIONARY, MENAMPUNG DATA
        dictionary = {
            'dataForm'   : form
        }

        return render(request, 'kembali/non/tambah.html', dictionary)
    
    else :
        return redirect('login/')

def updateN(request, id_kembali) :

    if 'user_id' in request.session :

        instanceKembaliN = get_object_or_404(tabelKembaliN, noKembaliN=id_kembali)

        if request.method == 'POST':
            form = formKembaliN(request.POST, instance=instanceKembaliN)
            if form.is_valid():

                save = form.save(commit=False)
                
                formPinjam          = request.POST.get('noPinjamN')
                instancePinjam      = tabelPinjamN.objects.get(noPinjamN=formPinjam)
                tglKembali          = instancePinjam.tglKembali
                save.tglKembali     = tglKembali

                tglPengembalian     = form.cleaned_data['tglPengembalian']
                selisih_hari        = tglPengembalian - tglKembali

                if selisih_hari.days > 0:
                    denda = selisih_hari.days * 500
                else:
                    denda = 0
                
                # Set the foreign key values
                save.denda = denda;

                save.noPinjamN      = form.cleaned_data['noPinjamN']
                save.kodePetugas    = form.cleaned_data['kodePetugas']

                # Save the form
                save.save()

                return redirect('../../')
        else:
            form =formKembaliN(instance=instanceKembaliN)
            form.fields['noPinjamN'].initial = instanceKembaliN.noPinjamN

        dictionary  = {
            'dataForm'      : form,
            # 'dataKembaliN'   : instanceKembaliN,
        }

        return render(request, 'kembali/non/update.html', dictionary)
    
    else :
        return redirect('login/')

def hapusN(request, id_kembali):

    if 'user_id' in request.session :

        instanceKembaliN = get_object_or_404(tabelKembaliN, noKembaliN=id_kembali)

        if instanceKembaliN.delete() :
            return redirect('../../')
        else:
            dictionary = {
                'error_message': 'Data tidak dihapus.'
            }

        return render(request, 'kembali/non/index.html', dictionary)
    
    else :
        return redirect('login/')
