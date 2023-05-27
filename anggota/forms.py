from django import forms
from . models import anggotaSiswa

class formAnggotaSiswa(forms.ModelForm):
    class Meta:
        model = anggotaSiswa
        fields = ['nim', 'nama', 'jurusan','tanggal_lahir','alamat','kode_post','hp']
        widgets = {
            'nim'   : forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan nim'}),
            'nama'  : forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan nama'}),
            'jurusan'  : forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan jurusan'}),
            'tanggal_lahir'  : forms.DateInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan tanggal_lahir','type':'date'}),
            'alamat'  : forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan alamat'}),
            'kode_post'  : forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan kode post'}),
            'hp'  : forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan hp'}),
        }
