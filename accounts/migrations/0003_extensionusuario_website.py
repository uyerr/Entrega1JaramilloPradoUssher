# Generated by Django 4.1.1 on 2022-11-08 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_extensionusuario_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='extensionusuario',
            name='website',
            field=models.CharField(max_length=100, null=True),
        ),
    ]