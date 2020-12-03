from django.contrib import admin
from django.urls import path
from perpustakaan.views import buku,tambahBuku




urlpatterns = [
    path('admin/', admin.site.urls),
    path('buku/', buku),
    path('tambah-buku/', tambahBuku),
    # path('penerbit/', penerbit),
    # path('', views.index, name='index'),
]
