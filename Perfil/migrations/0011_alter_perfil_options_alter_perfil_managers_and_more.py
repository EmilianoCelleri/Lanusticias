# Generated by Django 4.0.5 on 2022-08-05 20:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Perfil', '0010_alter_perfil_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='perfil',
            options={},
        ),
        migrations.AlterModelManagers(
            name='perfil',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='user_ptr',
        ),
        migrations.AddField(
            model_name='perfil',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='perfil',
            name='descripcion',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='web',
            field=models.URLField(blank=True, null=True),
        ),
    ]
