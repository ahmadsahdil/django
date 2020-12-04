from django.contrib import admin
from django.urls import path
from perpustakaan.views import *




urlpatterns = [
    path('admin/', admin.site.urls),
    path('buku/', buku),
    path('tambah-buku/', tambahBuku, name='tambah-buku'),
    path('buku/ubah/<int:id_buku>', ubahBuku , name='ubah_buku'),
    path('buku/hapus/<int:id_buku>', hapusBuku, name='hapus_buku'),
    # path('penerbit/', penerbit),
    # path('', views.index, name='index'),
]
