# Generated by Django 3.0.5 on 2022-04-06 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0004_auto_20220331_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(default='Producto', max_length=500),
        ),
    ]