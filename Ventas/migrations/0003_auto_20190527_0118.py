# Generated by Django 2.1.7 on 2019-05-27 01:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ventas', '0002_auto_20190525_0029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='Empleado',
        ),
        migrations.AlterField(
            model_name='venta',
            name='Cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuarios.Usuario'),
        ),
    ]