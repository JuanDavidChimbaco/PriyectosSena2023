# Generated by Django 4.2.1 on 2023-06-01 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catNombre', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venFecha', models.DateField()),
                ('venCliente', models.CharField(max_length=100)),
                ('venDireccion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proCodigo', models.IntegerField(unique=True)),
                ('proNombre', models.CharField(max_length=50)),
                ('proPrecio', models.IntegerField()),
                ('proCategoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appORM.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detCantidad', models.IntegerField()),
                ('detValorDetalle', models.IntegerField()),
                ('detProducto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appORM.producto')),
                ('detVenta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appORM.venta')),
            ],
        ),
    ]
