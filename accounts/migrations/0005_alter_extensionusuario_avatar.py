# Generated by Django 4.1.1 on 2022-12-12 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_extensionusuario_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extensionusuario',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='media/avatar'),
        ),
    ]
