# Generated by Django 2.0.4 on 2018-05-04 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartolas', '0002_auto_20180428_0104'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartolas',
            options={'ordering': ['cartolaNome'], 'verbose_name': 'Cartola', 'verbose_name_plural': 'Cartolas'},
        ),
        migrations.AlterField(
            model_name='cartolas',
            name='cartolaNome',
            field=models.CharField(max_length=50, verbose_name='cartolaNome'),
        ),
        migrations.AlterField(
            model_name='cartolas',
            name='cartolaTime',
            field=models.CharField(max_length=50, verbose_name='cartolaTime'),
        ),
    ]