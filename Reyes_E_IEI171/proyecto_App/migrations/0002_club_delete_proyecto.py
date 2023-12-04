# Generated by Django 4.2.6 on 2023-12-04 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombresocio', models.CharField(max_length=50)),
                ('fechaincorporación', models.DateField()),
                ('añonacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=50)),
                ('sexo', models.CharField(max_length=50)),
                ('estado', models.IntegerField()),
                ('observacion', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Proyecto',
        ),
    ]
