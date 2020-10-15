# Generated by Django 3.1.2 on 2020-10-15 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_productimage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productimage',
            options={'verbose_name': 'Imagen producto', 'verbose_name_plural': 'Imagenes producto'},
        ),
        migrations.AddField(
            model_name='productimage',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='product-thumbnails'),
        ),
    ]
