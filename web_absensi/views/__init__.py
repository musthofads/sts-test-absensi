from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from ..models import *
from .tools import get_random_code
from .karyawan import *
from .absensi import *
from .forms import *


def registerView(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            user_form = UserForm(data=request.POST)
            if user_form.is_valid():
                email = request.POST.get('email')
                user = User.objects.filter(email = email).first()
                if not user:
                    user = user_form.save()
                    user.set_password(user.password)
                    user.is_staff = True
                    user.is_active = True
                    user.save()

                    karyawan = Karyawan()
                    karyawan.no_karyawan = "MDS"+str(get_random_code(6))
                    karyawan.divisi = request.POST.get('divisi')
                    karyawan.jabatan = request.POST.get('jabatan')
                    karyawan.no_telepon = request.POST.get('no_telepon')
                    karyawan.user_id = user.id
                    karyawan.save()

                    messages.info(request, 'Registrasi Berhasil. Silahkan Login.')
                else:
                    messages.info(request, 'Email sudah digunakan user '+user.username)
            else:
                print(user_form.errors)
                messages.info(request, 'Registrasi Gagal')
        else:
            user_form = UserForm()

    return render(request,'register.html')


def loginView(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = User.objects.filter(email = email).first()
            if user:
                username = user.username
                if username and password:
                    user = authenticate(request, username=username, password=password)
                    if user is not None:
                        login(request, user)
                        return redirect('home')
            else:
                messages.info(request, 'Login Gagal. Mohon periksa kembali Username dan Password')

    return render(request, 'login.html')

def LogoutView(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')