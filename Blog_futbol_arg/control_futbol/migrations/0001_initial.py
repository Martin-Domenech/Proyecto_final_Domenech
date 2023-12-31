# Generated by Django 4.2.6 on 2023-11-06 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=256)),
                ('ubicacion', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='entrenador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('apellido', models.CharField(max_length=256)),
                ('club', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('apellido', models.CharField(max_length=256)),
                ('club', models.CharField(max_length=256)),
                ('altura', models.IntegerField()),
                ('peso', models.IntegerField()),
            ],
        ),
    ]
