from django import forms
from . models import tabelBuku

class formBuku(forms.ModelForm):
    class Meta:
        model = tabelBuku
        fields = ['judul', 'penerbit', 'pengarang', 'thnterbit',  'kotaterbit', 'bahasa', 'edisi', 'deskripsi']
        widgets = {
            'judul'      : forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan judul'}),
            'penerbit'   : forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan penerbit'}),
            'pengarang' : forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan pengarang '}),
            'thnterbit'  : forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan thnterbit'}),
            'kotaterbit' : forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan kotaterbit'}),
            'bahasa'    : forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan bahas'}),
            'edisi'     : forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan edisi'}),
            'deskripsi' : forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan deskripsi'}),
        }
