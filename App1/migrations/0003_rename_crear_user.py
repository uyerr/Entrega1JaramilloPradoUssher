# Generated by Django 4.1.2 on 2022-10-17 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0002_rename_crear_usuarios_crear_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Crear',
            new_name='User',
        ),
    ]
