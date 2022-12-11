# Generated by Django 4.1.3 on 2022-12-11 03:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppUsuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostCriticas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=90)),
                ('sub_titulo', models.CharField(max_length=90)),
                ('fecha', models.DateField()),
                ('texto', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Posteo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=90)),
                ('subtitulo', models.CharField(max_length=90)),
                ('texto', models.CharField(max_length=254)),
                ('nombre', models.CharField(max_length=90)),
                ('email', models.CharField(max_length=50)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostNoticias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=90)),
                ('sub_titulo', models.CharField(max_length=90)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('texto', models.CharField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='login',
        ),
    ]
