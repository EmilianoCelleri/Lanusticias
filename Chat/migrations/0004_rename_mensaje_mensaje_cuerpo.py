# Generated by Django 4.0.5 on 2022-08-03 00:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Chat', '0003_usuarios_nombre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mensaje',
            old_name='mensaje',
            new_name='cuerpo',
        ),
    ]
