# Generated by Django 3.2.6 on 2021-08-31 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ppid', '0004_alter_form_information_information'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form_information',
            name='Information',
            field=models.TextField(blank=True, null=True),
        ),
    ]
