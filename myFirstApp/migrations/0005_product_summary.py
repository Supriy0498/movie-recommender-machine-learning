# Generated by Django 3.0.8 on 2020-07-01 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myFirstApp', '0004_auto_20200701_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='summary',
            field=models.TextField(default='Good summary'),
            preserve_default=False,
        ),
    ]