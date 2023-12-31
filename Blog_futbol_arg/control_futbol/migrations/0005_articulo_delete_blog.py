# Generated by Django 4.2.6 on 2023-11-22 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_futbol', '0004_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=256)),
                ('titulo', models.CharField(max_length=256)),
                ('subtitulo', models.CharField(max_length=256)),
                ('cuerpo', models.CharField(max_length=1200)),
                ('fecha', models.CharField(max_length=64)),
            ],
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
