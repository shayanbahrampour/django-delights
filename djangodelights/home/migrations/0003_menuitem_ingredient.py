# Generated by Django 4.0.4 on 2022-04-19 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_unit_price_ingredient_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='ingredient',
            field=models.ManyToManyField(to='home.ingredient'),
        ),
    ]
