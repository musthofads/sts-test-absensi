from django.shortcuts import render, redirect
from .forms import *
from .tools import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from ..models import *
from django.contrib import messages

@login_required(login_url='login')
def karyawan_list(request):
    users = User.objects.filter(is_superuser=False).all().select_related("karyawan")
    list_karyawan = []
    for user in users:
        data = dict(
            id=user.id,
            no_karyawan=user.karyawan.no_karyawan,
            first_name=user.first_name,
            last_name=user.last_name,
            divisi=user.karyawan.divisi,
            jabatan=user.karyawan.jabatan,
            is_active=user.is_active,
        )
        list_karyawan.append(data)

    context = {'karyawan_list': list_karyawan}

    return render(request, "karyawan/karyawan_list.html", context)


@login_required(login_url='login')
def karyawan_add(request):  
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            user = User.objects.filter(email = email).first()
            if not user:
                user = form.save()
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

                messages.info(request, 'Tambah Karyawan Berhasil')
            else:
                messages.info(request, 'Email sudah digunakan user '+user.username)
        else:
            print(form.errors)
            messages.info(request, 'Tambah Karyawan Gagal')
    else:
        form = UserForm()

    return render(request,'karyawan/karyawan_form.html',{'form':form})  


@login_required(login_url='login')
def karyawan_update(request, id):
    user = User.objects.get(id=id)
    if request.method == "GET":
        data = dict(
            id=user.id,
            email=user.email,
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            divisi=user.karyawan.divisi,
            jabatan=user.karyawan.jabatan,
            no_telepon=user.karyawan.no_telepon,
            is_active=user.is_active,
        )
    else:
        if request.method == 'POST':
            form = UserForm(data=request.POST, instance=user)
            if form.is_valid():
                user.set_password(request.POST.get('password'))
                user.email = request.POST.get('email')
                user.username = request.POST.get('username')
                user.first_name = request.POST.get('first_name')
                user.last_name = request.POST.get('last_name')
                user.is_staff = True
                user.is_active = True
                user.save()

                karyawan = Karyawan.objects.get(user_id=id)
                karyawan.divisi = request.POST.get('divisi')
                karyawan.jabatan = request.POST.get('jabatan')
                karyawan.no_telepon = request.POST.get('no_telepon')
                karyawan.save()

                data = dict(
                    id=user.id,
                    email=user.email,
                    username=user.username,
                    first_name=user.first_name,
                    last_name=user.last_name,
                    divisi=user.karyawan.divisi,
                    jabatan=user.karyawan.jabatan,
                    no_telepon=user.karyawan.no_telepon,
                    is_active=user.is_active,
                )
                messages.info(request, 'Update Karyawan Berhasil')
            else:
                print(form.errors)
                messages.info(request, 'Update Karyawan Gagal')
        else:
            form = UserForm()

    return render(request,'karyawan/karyawan_update.html', {'karyawan':data})


@login_required(login_url='login')
def karyawan_delete(request,id):
    karyawan = User.objects.get(pk=id)
    karyawan.delete()
    messages.info(request, 'Data Berhasil Dihapus')
    return redirect('/karyawan')
