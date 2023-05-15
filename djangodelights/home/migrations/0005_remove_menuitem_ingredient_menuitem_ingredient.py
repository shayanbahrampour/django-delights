# Generated by Django 4.0.4 on 2022-04-19 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_menuitem_ingredient_menuitem_ingredient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='ingredient',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='ingredient',
            field=models.ManyToManyField(to='home.ingredient'),
        ),
    ]