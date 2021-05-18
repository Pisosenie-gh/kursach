# Generated by Django 3.2.3 on 2021-05-18 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, verbose_name='Название категории')),
                ('description', models.CharField(blank=True, max_length=500, verbose_name='Описание категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, verbose_name='Название обуви')),
                ('description', models.CharField(blank=True, max_length=500, verbose_name='Описание обуви')),
                ('date', models.DateTimeField(blank=True, null=True, verbose_name='Дата')),
                ('price', models.PositiveIntegerField(blank=True, verbose_name='Цена')),
                ('size', models.PositiveIntegerField(blank=True, verbose_name='Размер')),
                ('color', models.CharField(blank=True, max_length=500, verbose_name='Цвет обуви')),
                ('image', models.ImageField(blank=True, upload_to='photo', verbose_name='Image')),
                ('image_2', models.ImageField(blank=True, upload_to='photo', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Обувь',
                'verbose_name_plural': 'Обувь',
            },
        ),
    ]