from django.shortcuts import render
from perpustakaan.models import Buku
from perpustakaan.forms import formBuku

def buku(request):
    books = Buku.objects.all()
    konteks = {
        'books' : books,
    }
    return render(request,'buku.html',konteks)

def tambahBuku(request):
    form = formBuku()
    konteks = {
        'form' : form,
    }

    return render(request,'tambah-buku.html',konteks)
