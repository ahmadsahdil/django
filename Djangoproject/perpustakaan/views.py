from django.shortcuts import render
from perpustakaan.models import Buku
from perpustakaan.forms import formBuku


def buku(request):
    # menampilkan beberapa data 'where di sql' pisahkan dengan "__"
    # limit data yang ditampilakan gunakan "[:3]" di akhir
    books = Buku.objects.filter(kelompok_id_id__nama='ahmad')[:3]
    # Menampilkan semua data
    # books = Buku.objects.all()
    konteks = {
        'books': books,
    }
    return render(request, 'buku.html', konteks)


def tambahBuku(request):
    if request.POST:
        form = formBuku(request.POST)
        if form.is_valid():
            form.save()
            form = formBuku()
            pesan = "Data berhasil Disimpan"
            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-buku.html', konteks)

    else:

        form = formBuku()
        konteks = {
            'form': form,
        }
        return render(request, 'tambah-buku.html', konteks)
