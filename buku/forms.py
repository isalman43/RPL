from django import forms
from . models import tabelBuku

class formBuku(forms.ModelForm):
    class Meta:
        model = tabelBuku
        fields = ['judul', 'penerbit', 'pengarang', 'thnterbit',  'kotaterbit', 'bahasa', 'edisi', 'deskripsi']
        widgets = {
            'judul'         : forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Judul'}),
            'penerbit'      : forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Penerbit'}),
            'pengarang'     : forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Pengarang '}),
            'thnterbit'     : forms.NumberInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Tahun Terbit', 'type' : 'number', 'min' : '1900', 'max' : '2999'}),
            'kotaterbit'    : forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Kota Terbit'}),
            'bahasa'        : forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Bahasa'}),
            'edisi'         : forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Edisi'}),
            'deskripsi'     : forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Deskripsi', 'type' : 'text'}),
        }
