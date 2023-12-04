# Generated by Django 4.2.6 on 2023-12-04 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaInicio', models.DateField()),
                ('fechaTermino', models.DateField()),
                ('nombre', models.CharField(max_length=50)),
                ('responsable', models.CharField(max_length=50)),
                ('prioridad', models.IntegerField()),
            ],
        ),
    ]