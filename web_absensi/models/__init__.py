from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Karyawan(models.Model):
    user = models.OneToOneField(User, related_name='karyawan', on_delete=models.CASCADE, unique=True)
    no_karyawan = models.CharField(max_length=255)
    divisi = models.CharField(max_length=255)
    jabatan = models.CharField(max_length=255)
    no_telepon = models.CharField(max_length=255)

    class Meta:
        db_table = 'karyawan'

class Absensi(models.Model):
    user_id = models.IntegerField()
    tanggal = models.DateTimeField(blank=True, null=True)
    jam_masuk = models.TimeField()
    jam_keluar = models.TimeField()
    status_checkin = models.BooleanField()

    class Meta:
        db_table = 'absensi'