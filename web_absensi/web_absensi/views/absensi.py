from django.shortcuts import render, redirect
from .forms import *
from .tools import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from ..models import *
from django.contrib import messages
import time
from datetime import datetime, timedelta, date

@login_required(login_url='login')
def absensi(request):
    print(request.user.id)
    user = User.objects.get(id=request.user.id)
    data = dict(
        id=user.id,
        nama=user.first_name+' '+user.last_name,
        divisi=user.karyawan.divisi,
        jabatan=user.karyawan.jabatan
    )

    absen = Absensi.objects.filter(user_id=request.user.id).order_by('id').reverse().first()
    if absen:
        if absen.status_checkin != True:
            data.update({'checkin': True})
        else:
            data.update({'checkin': False})
    else:
        data.update({'checkin': True})
    print(data)
    context = {'karyawan': data}

    return render(request, "absensi.html", context)


@login_required(login_url='login')
def checkin(request):
    user = User.objects.get(id=request.user.id)
    data = dict(
        id=user.id,
        nama=user.first_name+' '+user.last_name,
        divisi=user.karyawan.divisi,
        jabatan=user.karyawan.jabatan
    )

    today = datetime.now()
    time = today.strftime("%H:%M:%S")

    absen = Absensi()
    absen.user_id = user.id
    absen.tanggal = today
    absen.jam_masuk = time
    absen.jam_keluar = "00:00:00"
    absen.status_checkin = True
    absen.save()
    data.update({'checkin': True})

    context = {'karyawan': data}
    render(request, "absensi.html", context)
    return redirect('/absensi')

@login_required(login_url='login')
def checkout(request):
    user = User.objects.get(id=request.user.id)
    data = dict(
        id=user.id,
        nama=user.first_name+' '+user.last_name,
        divisi=user.karyawan.divisi,
        jabatan=user.karyawan.jabatan
    )

    absen = Absensi.objects.filter(user_id=request.user.id).order_by('id').reverse().first()
    if absen:
        today = datetime.now()
        time = today.strftime("%H:%M:%S")
        absen.jam_keluar = time
        absen.status_checkin = False
        absen.save()
        data.update({'checkin': False})

    context = {'karyawan': data}
    render(request, "absensi.html", context)
    return redirect('/absensi')

@login_required(login_url='login')
def log_absensi(request):
    if request.user.is_superuser:
        users = User.objects.filter(is_superuser=False).all().select_related("karyawan")
        list_logabsensi = []
        for user in users:
            absens = Absensi.objects.filter(user_id=user.id).reverse().all()
            for absen in absens:
                jam_masuk = absen.jam_masuk.strftime("%H:%M:%S")
                jam_masuk = datetime.strptime(jam_masuk, "%H:%M:%S")
                jam_keluar = absen.jam_keluar.strftime("%H:%M:%S")
                jam_keluar = datetime.strptime(jam_keluar, "%H:%M:%S")

                if absen.jam_keluar.strftime("%H:%M:%S") == "00:00:00":
                    lama_kerja = "Sedang Bekerja"
                else:
                    lama_kerja = jam_keluar - jam_masuk
                    lama_kerja = datetime.strptime(str(lama_kerja), "%H:%M:%S")
                    lama_kerja = lama_kerja.strftime("%H Jam %M Menit")
                print(str(lama_kerja))
                data = dict(
                    first_name = user.first_name,
                    last_name = user.last_name,
                    divisi = user.karyawan.divisi,
                    jabatan = user.karyawan.jabatan,
                    tanggal = dMy(absen.tanggal),
                    jam_masuk = absen.jam_masuk.strftime("%H:%M:%S"),
                    jam_keluar = absen.jam_keluar.strftime("%H:%M:%S"),
                    lama_kerja = str(lama_kerja),
                )
                list_logabsensi.append(data)

    else:
        user = User.objects.get(id=request.user.id)
        absens = Absensi.objects.filter(user_id=request.user.id).all().order_by('id').reverse()

        list_logabsensi = []
        for absen in absens:
            jam_masuk = absen.jam_masuk.strftime("%H:%M:%S")
            jam_masuk = datetime.strptime(jam_masuk, "%H:%M:%S")
            jam_keluar = absen.jam_keluar.strftime("%H:%M:%S")
            jam_keluar = datetime.strptime(jam_keluar, "%H:%M:%S")

            if absen.jam_keluar.strftime("%H:%M:%S") == "00:00:00":
                lama_kerja = "Sedang Bekerja"
            else:
                lama_kerja = jam_keluar - jam_masuk
                lama_kerja = datetime.strptime(str(lama_kerja), "%H:%M:%S")
                lama_kerja = lama_kerja.strftime("%H Jam %M Menit")
            print(str(lama_kerja))
            data = dict(
                first_name = user.first_name,
                last_name = user.last_name,
                divisi = user.karyawan.divisi,
                jabatan = user.karyawan.jabatan,
                tanggal = dMy(absen.tanggal),
                jam_masuk = absen.jam_masuk.strftime("%H:%M:%S"),
                jam_keluar = absen.jam_keluar.strftime("%H:%M:%S"),
                lama_kerja = str(lama_kerja),
            )
            list_logabsensi.append(data)

    context = {'karyawan_list': list_logabsensi}

    return render(request, "absensi_log.html", context)
