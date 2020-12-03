from django.contrib import admin
from perpustakaan.models import Buku, Kelompok

class bukuAdmin(admin.ModelAdmin):
    list_display = ['judul','penulis','penerbit','jumlah']
    search_fields = ['judul','penulis','penerbit']
    list_filter = ('kelompok_id_id',)
    list_per_page = 2


admin.site.register(Buku, bukuAdmin)
admin.site.register(Kelompok)