# Generated by Django 3.2 on 2021-06-16 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_orderservices_choice_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderservices',
            name='choice_service',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Замовлення послуги'),
        ),
    ]
