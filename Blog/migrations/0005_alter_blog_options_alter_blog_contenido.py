# Generated by Django 4.0.5 on 2022-07-28 21:46

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_alter_blog_subtitulo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-creado']},
        ),
        migrations.AlterField(
            model_name='blog',
            name='contenido',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
