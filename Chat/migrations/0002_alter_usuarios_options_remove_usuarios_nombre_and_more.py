# Generated by Django 4.0.5 on 2022-08-02 23:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuarios',
            options={'verbose_name': 'Usuario'},
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='nombre',
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
