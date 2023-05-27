from django import forms
from . models import tabelSiswa, tabelNon

class formSiswa(forms.ModelForm):
    class Meta:
        model = tabelSiswa
        fields = ['nis', 'nama', 'jurusan','tanggal_lahir','alamat','kode_post','hp']
        widgets = {
            'nis'           : forms.NumberInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan NIS','type':'number'}),
            'nama'          : forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Nama'}),
            'jurusan'       : forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Jurusan'}),
            'tanggal_lahir' : forms.DateInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Tanggal Lahir','type':'date'}),
            'alamat'        : forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Alamat'}),
            'kode_post'     : forms.NumberInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Kode Post','type':'number'}),
            'hp'            : forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Hp','type':'number'}),
        }

class formNon(forms.ModelForm):
    class Meta:
        model = tabelNon
        fields = ['nip', 'nama', 'jabatan','tanggal_lahir','alamat','kode_post','hp']
        widgets = {
            'nip'           : forms.NumberInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan NIP','type':'number'}),
            'nama'          : forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Nama'}),
            'jabatan'       : forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Jabatan'}),
            'tanggal_lahir' : forms.DateInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Tanggal Lahir','type':'date'}),
            'alamat'        : forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Alamat'}),
            'kode_post'     : forms.NumberInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Kode Post','type':'number'}),
            'hp'            : forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Hp','type':'number'}),
        }