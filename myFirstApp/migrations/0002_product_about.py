# Generated by Django 3.0.8 on 2020-07-01 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myFirstApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='about',
            field=models.TextField(default='We are Developers'),
        ),
    ]