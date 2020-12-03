from django.forms import ModelForm
from django import forms
from perpustakaan.models import Buku

class formBuku(ModelForm):
    class Meta:
        model = Buku
        # fields = '__all__'
        exclude = ['penerbit']

        widgets = {
            'judul' : forms.TextInput({'class':'form-control'}),
            'penulis' : forms.TextInput({'class':'form-control'}),
            'penerbit' : forms.TextInput({'class':'form-control'}),
            'jumlah' : forms.NumberInput({'class':'form-control'}),
            'kelompok_id_id' : forms.Select({'class':'form-control'}),
        }