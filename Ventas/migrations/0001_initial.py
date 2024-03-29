# Generated by Django 2.1.7 on 2019-05-23 16:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Inventario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LineaVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subtotal', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Cantidad', models.IntegerField(blank=True, null=True)),
                ('IVA', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('Total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('IVATotal', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.AddField(
            model_name='lineaventa',
            name='Venta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ventas.Venta'),
        ),
    ]
