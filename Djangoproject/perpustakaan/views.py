from django.shortcuts import render, redirect
from perpustakaan.models import Buku
from perpustakaan.forms import formBuku
from django.contrib import messages

def ubahBuku(request, id_buku):
    buku = Buku.objects.get(id=id_buku)
    template = 'ubah-buku.html'
    if request.POST:
        form = formBuku(request.POST, instance=buku)
        if form.is_valid:
            messages.success(request,"Data berhasil Diedit")
            form.save()
            return redirect('ubah_buku',id_buku = id_buku)
    else:
        form = formBuku(instance=buku)
        konteks = {
            'form':form,
            'buku':buku,
        }
        return render(request,template,konteks)

def buku(request):
    # menampilkan beberapa data 'where di sql' pisahkan dengan "__"
    # limit data yang ditampilakan gunakan "[:3]" di akhir
    # books = Buku.objects.filter(kelompok_id_id__nama='ahmad')[:3]
    # Menampilkan semua data
    books = Buku.objects.all()
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
