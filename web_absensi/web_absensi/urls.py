from django.conf.urls import include, url
from django.urls import path
from rest_framework import routers
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('register', registerView, name='register'),
    # Login and Logout
    path('login', loginView, name="login"),
    path('logout', LogoutView, name='logout'),
    path('', home, name="home"),

    # User
    path('karyawan', karyawan_list, name='karyawan_list'),
    path('karyawan/add', karyawan_add, name='karyawan_insert'),
    path('karyawan/update/<int:id>', karyawan_update, name='karyawan_update'),
    path('karyawan/delete/<int:id>', karyawan_delete, name='karyawan_delete'),

    path('absensi', absensi, name='absensi'),
    path('checkin', checkin, name='checkin'),
    path('checkout', checkout, name='checkout'),
    path('absensi/log', log_absensi, name='log_absensi'),
    # path('register', RegisterAPI.as_view(), name='register'),
    # path('login', LoginAPI.as_view(), name='login'),
    # path('logout', knox_views.LogoutView.as_view(), name='logout'),
    # path('change_password', ChangePasswordView.as_view(), name='change_password'),
    # # path('reset-password', include('django_rest_passwordreset.urls', namespace='password_reset')),

    # path('reset_password',
    #  auth_views.PasswordResetView.as_view(),
    #  name="reset_password"),

    # path('reset_password_sent', 
    #     auth_views.PasswordResetDoneView.as_view(), 
    #     name="password_reset_done"),

    # path('reset/<uidb64>/<token>',
    #  auth_views.PasswordResetConfirmView.as_view(), 
    #  name="password_reset_confirm"),

    # path('reset_password_complete', 
    #     auth_views.PasswordResetCompleteView.as_view(), 
    #     name="password_reset_complete"),

]
