# Generated by Django 2.0 on 2019-12-18 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_desc',
        ),
    ]
