# Generated by Django 3.1.2 on 2020-10-16 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax_shipping', models.DecimalField(decimal_places=2, help_text='Fee de entrega', max_digits=9)),
                ('pvp_iva', models.BooleanField(default=False, help_text='Precio venta incluye iva')),
            ],
            options={
                'verbose_name': 'Configuracion Tienda',
                'db_table': 'base_shop',
            },
        ),
    ]