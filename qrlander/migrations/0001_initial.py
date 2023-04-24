# Generated by Django 3.2.18 on 2023-04-24 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='empleados/')),
            ],
        ),
        migrations.CreateModel(
            name='Visitante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('empresa', models.CharField(max_length=100)),
                ('motivo', models.CharField(max_length=200)),
                ('fecha_ingreso', models.DateTimeField(auto_now_add=True)),
                ('fecha_salida', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_ingreso', models.DateTimeField(auto_now_add=True)),
                ('fecha_salida', models.DateTimeField(blank=True, null=True)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qrlander.empleado')),
            ],
        ),
    ]