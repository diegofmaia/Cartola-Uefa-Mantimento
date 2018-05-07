# Generated by Django 2.0.4 on 2018-04-28 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cartolas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cartolaNome', models.CharField(max_length=50, verbose_name='Nome')),
                ('cartolaTime', models.CharField(max_length=50, verbose_name='Nome')),
                ('image', models.ImageField(blank=True, null=True, upload_to='cartolas/images', verbose_name='Imagem')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
        ),
    ]
