# Generated by Django 3.2.6 on 2021-08-31 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ppid', '0006_form_information_dinas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form_information',
            name='ktp',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='form_information',
            name='status',
            field=models.CharField(choices=[('Belum Diproses', 'Belum Diproses'), ('Sedang Diproses', 'Sedang Diproses'), ('Dikirimkan', 'Dikirimkan'), ('Ditolak', 'Ditolak')], max_length=125),
        ),
    ]
