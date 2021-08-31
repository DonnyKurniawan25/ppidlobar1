from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from ppid import models 
from django.core.exceptions import ValidationError

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class DataForm(ModelForm):
	class Meta:
		model = models.Data
		fields = '__all__'
		widgets = {
			'code': forms.TextInput(
				attrs = {
				'placeholder': 'Contoh DISHUB-001'
				}
			), 
            'title': forms.TextInput(
				attrs = {
				'placeholder': 'Judul DIP'
				}
			), 
            'information': forms.Textarea(
				attrs = {
				'placeholder': 'Deskripsi'
				}
			), 
            # 'file': forms.FileInput(
			# 	attrs = {
			# 	'style': 'width:92%;'
			# 	}
			# ), 
            'date_a': forms.DateInput(
				attrs = {
				'id': 'kalender',
                'style': 'width:92%; margin-left:10px'
				}
			), 
            'date_b': forms.DateInput(
				attrs = {
				'id': 'kalender2',
                'style': 'width:92%; margin-left:10px'
				}
			), 
		}

	def clean_code(self):
		code = self.cleaned_data.get('code')
		if (code == ""):
			raise forms.ValidationError('Kode Tidak Boleh Kosong')
		for instance in models.Data.objects.all():
			if instance.code == code:
				raise forms.ValidationError('Kode Sudah Pernah Digunakan')
		return code

class RequestForm(ModelForm):
    class Meta:
        model = models.Form_information
        fields = '__all__'
        widgets = {
			'name': forms.TextInput(
				attrs = {
				'placeholder': 'Nama Lengkap',
                'class' : 'form-control',
				'readonly' : ''
				}
			), 
            'kategory_pemohon': forms.TextInput(
				attrs = {
				'type':'hidden',
				}
			), 
            'address': forms.Textarea(
				attrs = {
				'placeholder': 'Alamat',
				'readonly' : ''
				}
			), 
            'telp': forms.TextInput(
				attrs = {
				'placeholder': 'No Telp',
				'type': 'number',
                'class' : 'form-control',
				'readonly' : ''
				}
			), 
            'email': forms.TextInput(
				attrs = {
				'placeholder': 'Email',
                'class' : 'form-control',
				'readonly' : ''
				}
			), 
            'purpose': forms.Textarea(
				attrs = {
				'placeholder': 'Tujuan Penggunaan Informasi',
				'readonly' : ''
				}
			), 
             'detail': forms.Textarea(
				attrs = {
				'placeholder': 'Detail Informasi Yang Dibutuhkan',
				'readonly' : ''
				}
			), 
            'action': forms.TextInput(
				attrs = {
				'type':'hidden',
				}
			), 
            'status': forms.Select(
				attrs = {
                'class':'form-control'
				}
			), 
            'dinas': forms.Select(
				attrs = {
				'readonly' : ''
				}
			), 
			'ktp': forms.FileInput(
				attrs = {
				'type': 'hidden'
				}
			), 
		}

		






