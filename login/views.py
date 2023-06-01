from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
import hashlib
# from django import forms


from . forms import formLogin
from petugas.models import tabelPetugas

def index(request):
    if request.method == 'POST':

        form = formLogin(request.POST)

        # if form.is_valid():

            # Ambil data yang diisi oleh pengguna
        username = request.POST.get('username')

            # AMBIL DATA PASSWORD
        password = request.POST.get('password')
            # ENSKRIPSI PASSWORD
        hashed_password = hashlib.md5(password.encode()).hexdigest()

        try:
            petugas = tabelPetugas.objects.get(username=username, password=hashed_password)
            if petugas.username == username and petugas.password == hashed_password:

                request.session['user_id']  = petugas.kodePetugas
                request.session['username'] = petugas.username

                return redirect('../')
            else:
                messages.error(request, 'Username atau Password Salah')
        except tabelPetugas.DoesNotExist:
            messages.error(request, 'Akun tidak ditemukan')
                # messages.error(request, f"Username atau Password Salah. Hashed Password: {hashed_password}")
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
        
        # else:
        #     print(form.errors)
        #     messages.error(request, 'Form tidak valid')

    else:
        form = formLogin()

    context = {
        'dataForm': form
    }
    
    return render(request, 'login/index.html', context)

def logout_view(request):
    logout(request)
    return redirect('../')
