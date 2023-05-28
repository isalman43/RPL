from django import forms
from django.utils import timezone
from datetime import timedelta

from .models import tabelPinjamS, tabelPinjamN

from anggota.models import tabelSiswa, tabelNon
from petugas.models import tabelPetugas
from buku.models import tabelBuku

class formPinjamS(forms.ModelForm):
    no_anggota  = forms.ModelChoiceField(queryset=tabelSiswa.objects.all(), widget=forms.Select(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan No Anggota Siswa'}))
    kodePetugas = forms.ModelChoiceField(queryset=tabelPetugas.objects.all(), widget=forms.Select(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Kode Petugas'}))
    kodebuku    = forms.ModelChoiceField(queryset=tabelBuku.objects.all(), widget=forms.Select(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Kode Buku'}))

    class Meta:
        model = tabelPinjamS
        fields = ['tglPinjam', 'tglKembali', 'jumlah']
        widgets = {
            'tglPinjam' : forms.DateInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Tanggal Pinjam', 'type' : 'date'}),
            'tglKembali': forms.DateInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Tanggal Kembali', 'type' : 'date'}),
            'jumlah'    : forms.NumberInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Jumlah', 'type' : 'number', 'min' : '1', 'max' : '3'}),
        }
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tglPinjam'].initial = timezone.now().date()
        self.fields['tglKembali'].initial = (timezone.now() + timedelta(days=7)).date()

class formPinjamN(forms.ModelForm):
    no_anggotaN = forms.ModelChoiceField(queryset=tabelNon.objects.all(), widget=forms.Select(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan No Anggota Non Siswa'}))
    kodePetugas = forms.ModelChoiceField(queryset=tabelPetugas.objects.all(), widget=forms.Select(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Kode Petugas'}))
    kodebuku    = forms.ModelChoiceField(queryset=tabelBuku.objects.all(), widget=forms.Select(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Kode Buku'}))

    class Meta:
        model = tabelPinjamN
        fields = ['tglPinjam', 'tglKembali', 'jumlah']
        widgets = {
            'tglPinjam' : forms.DateInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Tanggal Pinjam', 'type' : 'date'}),
            'tglKembali': forms.DateInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Tanggal Kembali', 'type' : 'date'}),
            'jumlah'    : forms.NumberInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Jumlah', 'type' : 'number', 'min' : '1', 'max' : '3'}),
        }
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tglPinjam'].initial = timezone.now().date()
        self.fields['tglKembali'].initial = (timezone.now() + timedelta(days=7)).date()