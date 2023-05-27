from django import forms
from petugas.models import tabelPetugas

class formLogin(forms.ModelForm):
    class Meta:
        model = tabelPetugas
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Username'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Password'}),
        }