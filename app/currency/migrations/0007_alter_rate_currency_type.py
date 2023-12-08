# Generated by Django 4.2.7 on 2023-12-08 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0006_rename_type_rate_currency_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='currency_type',
            field=models.SmallIntegerField(choices=[(1, 'Dollar'), (2, 'Euro'), (3, 'Złoty')], default=1, verbose_name='Currency type'),
        ),
    ]
