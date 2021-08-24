from django.db import models
from django.db.models.fields import CharField
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify


# Create your models here.

class Dinas(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name="dinas")
    title = models.CharField(max_length=225)
    shortness = CharField(max_length=50)
    def __str__(self):
        return self.title

class Type_data(models.Model):
    type = models.CharField(max_length=225)
    
    def __str__(self):
        return self.type

class Type_article(models.Model):
    title = models.CharField(max_length=225)
    def __str__(self):
        return self.title

class IpModel(models.Model):
    ip =models.CharField(max_length=225)

    def __str__(self):
        return self.ip

class Data(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    code = models.CharField(max_length=125, blank=True)
    title = models.CharField(max_length=225)
    slug = models.SlugField(max_length=255, default='', unique=True,
        blank=True, null=True)
    responsible = models.CharField(max_length=225)
    dinas = models.ForeignKey(Dinas, on_delete=models.CASCADE, null=True, blank=True) 
    information = models.CharField(max_length=225)
    date = models.DateField(auto_now_add=True)
    date_a = models.DateField()
    date_b = models.DateField()
    file = models.FileField()
    read = models.ManyToManyField(IpModel, related_name="post_views", blank=True, null=True)
    download = models.ManyToManyField(IpModel, related_name="post_download", blank=True, null=True)
    type_data = models.ForeignKey(Type_data, on_delete=models.CASCADE)
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



