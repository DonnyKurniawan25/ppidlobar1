from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.fields import CharField, NullBooleanField
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.contrib.sites.models import Site


# Create your models here.

class Dinas(models.Model):
    site = models.ForeignKey(Site, null=True, blank=True, on_delete=models.SET_NULL)
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL, related_name="dinas")
    title = models.CharField(max_length=225)
    shortness = CharField(max_length=50)
    def __str__(self):
        return self.title

class Type_data(models.Model):
    site = models.ForeignKey(Site, null=True, blank=True, on_delete=models.SET_NULL)
    type = models.CharField(max_length=225, null=True, blank=True)
    
    def __str__(self):
        return self.type

class IpModel(models.Model):
    site = models.ForeignKey(Site, null=True, blank=True, on_delete=models.SET_NULL)
    ip = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return self.ip

class Data(models.Model):
    site = models.ForeignKey(Site, null=True, blank=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    code = models.CharField(max_length=125, blank=True)
    title = models.CharField(max_length=225, null=True, blank=True)
    slug = models.SlugField(max_length=255, default='', unique=True,
        blank=True, null=True)
    responsible = models.CharField(max_length=225, null=True, blank=True)
    dinas = models.ForeignKey(Dinas, on_delete=models.SET_NULL, null=True, blank=True) 
    information = models.CharField(max_length=225, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    date_a = models.DateField(null=True, blank=True)
    date_b = models.DateField(null=True, blank=True)
    file = models.FileField(null=True, blank=True)
    read = models.ManyToManyField(IpModel, related_name="post_views", blank=True, null=True)
    download = models.ManyToManyField(IpModel, related_name="post_download", blank=True, null=True)
    type_data = models.ForeignKey(Type_data, on_delete=models.SET_NULL, null=True, blank=True)
    size = models.CharField(max_length=225, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Data, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)

    def total_reads(self):
        return self.read.count()

    def total_downloads(self):
        return self.download.count()

class Type_pemohon(models.Model):
    site = models.ForeignKey(Site, null=True, blank=True, on_delete=models.SET_NULL)
    type_pemohon = models.CharField(max_length=225, null=True, blank=True)
    
    def __str__(self):
        return self.type_pemohon

class Type_action(models.Model):
    site = models.ForeignKey(Site, null=True, blank=True, on_delete=models.SET_NULL)
    type_action = models.TextField(null=True, blank=True) 

    def __str__(self):
        return self.type_action
    
class Form_information(models.Model):
    site = models.ForeignKey(Site, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=255, null=True, blank=True)
    kategory_pemohon = models.ForeignKey(Type_pemohon, on_delete=models.SET_NULL, null=True, blank=True)
    action = models.ForeignKey(Type_action, on_delete=models.SET_NULL, null=True, blank=True)
    dinas = models.ForeignKey(Dinas, null=True, blank=True, on_delete=models.SET_NULL)
    address = models.TextField(null=True, blank=True)
    telp = models.CharField(max_length=25, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    ktp = models.FileField(null=True, blank=True)
    purpose = models.TextField(null=True, blank=True)
    detail = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    status_choice = (
        ('Belum Diproses','Belum Diproses'),
        ('Sedang Diproses', 'Sedang Diproses'),
        ('Dikirimkan', 'Dikirimkan'),
        ('Ditolak', 'Ditolak'),
    )
    status = models.CharField(max_length=125, choices=status_choice, null=True, blank=True)
    Information = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.purpose








