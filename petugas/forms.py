from django import forms
from . models import tabelPetugas

class formPetugas(forms.ModelForm):
    class Meta:
        model = tabelPetugas
        fields = ['nama', 'jabatan', 'username', 'password']
        widgets = {
            'nama'      : forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Nama'}),
            'jabatan'   : forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Jabatan'}),
            'username'  : forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Username'}),
            'password'  : forms.PasswordInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Password'}),
        }
