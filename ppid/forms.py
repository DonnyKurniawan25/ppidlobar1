from django.db.models import fields
from django.forms import ModelForm
from django import forms
from .models import Form_information
from django.core.exceptions import ValidationError

class RequestForm(ModelForm):
    class Meta:
        model = Form_information
        fields = '__all__'
        widgets = {
			'name': forms.TextInput(
				attrs = {
				'placeholder': 'Nama Lengkap',
                'class' : 'form-control'
				}
			), 
            'kategory_pemohon': forms.Select(
				attrs = {
				'placeholder': 'Kategori',
                'class' : 'form-control'
				}
			), 
            'address': forms.Textarea(
				attrs = {
				'placeholder': 'Alamat',
                'class' : 'form-control',
                'style' : 'resize:none;width:790px;height:120px;',
				}
			), 
            'telp': forms.TextInput(
				attrs = {
				'placeholder': 'No Telp',
				'type': 'number',
                'class' : 'form-control',
				}
			), 
            'email': forms.TextInput(
				attrs = {
				'placeholder': 'Email',
                'class' : 'form-control',
				}
			), 
            'ktp': forms.FileInput(
				attrs = {
				'placeholder': 'KTP',
                'class' : 'form-control',
				}
			), 
            'purpose': forms.Textarea(
				attrs = {
				'placeholder': 'Tujuan Penggunaan Informasi',
                'class' : 'form-control',
                'style' : 'resize:none;width:790px;height:120px;',
				}
			), 
             'detail': forms.Textarea(
				attrs = {
				'placeholder': 'Detail Informasi Yang Dibutuhkan',
                'class' : 'form-control',
                'style' : 'resize:none;width:790px;height:120px;',
				}
			), 
            'action': forms.Select(
				attrs = {
                'class' : 'form-control'
				}
			), 
            'status': forms.TextInput(
				attrs = {
                'type' : 'hidden',
                'value':'Belum Diproses'
				}
			), 
            'dinas': forms.Select(
				attrs = {
                'class':'form-control'
				}
			), 
		}

