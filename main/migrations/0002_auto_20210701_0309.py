# Generated by Django 3.2.4 on 2021-07-01 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicesandprice',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание RU'),
        ),
        migrations.AlterField(
            model_name='servicesandprice',
            name='service',
            field=models.CharField(max_length=200, verbose_name='Услуга RU'),
        ),
        migrations.AlterField(
            model_name='servicesandprice',
            name='serviceUA',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Послуга UA'),
        ),
        migrations.AlterField(
            model_name='servicesandprice',
            name='si',
            field=models.CharField(blank=True, default='грн', max_length=20, null=True, verbose_name='Единици измерения RU'),
        ),
    ]
