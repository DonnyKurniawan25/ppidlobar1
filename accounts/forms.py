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

		






