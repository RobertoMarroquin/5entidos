# Generated by Django 2.1.7 on 2019-05-27 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0002_auto_20190527_0118'),
        ('Ventas', '0003_auto_20190527_0118'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='Empleado',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='venta_Empleado', to='Usuarios.Usuario'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='venta',
            name='Cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='venta_Cliente', to='Usuarios.Usuario'),
        ),
    ]
