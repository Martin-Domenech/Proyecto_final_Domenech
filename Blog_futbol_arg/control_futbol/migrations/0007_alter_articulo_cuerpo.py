# Generated by Django 4.2.6 on 2023-11-24 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_futbol', '0006_alter_articulo_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='cuerpo',
            field=models.TextField(),
        ),
    ]