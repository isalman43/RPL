from django import forms
from django.utils import timezone

from . models import tabelKembaliS

from pinjam.models  import tabelPinjamS
from petugas.models  import tabelPetugas

class formKembaliS(forms.ModelForm):
    noPinjamS   = forms.ModelChoiceField(queryset=tabelPinjamS.objects.all(), widget=forms.Select(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan No Pinjam Siswa'}))
    kodePetugas = forms.ModelChoiceField(queryset=tabelPetugas.objects.all(), widget=forms.Select(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Kode Petugas'}))

    class Meta:
        model = tabelKembaliS
        fields = ['tglPengembalian']
        widgets = {
            # 'tglKembali'        : forms.DateInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Tanggal Kembali', 'type' : 'date'}),
            'tglPengembalian'   : forms.DateInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Tanggal Pengembalian', 'type' : 'date'}),
            # 'denda'             : forms.NumberInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Denda', 'type' : 'number'}),
        }
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tglPengembalian'].initial = timezone.now().date()
        