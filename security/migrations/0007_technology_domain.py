# Generated by Django 2.0 on 2019-12-26 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0006_auto_20191219_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='technology',
            name='domain',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='security.Domain'),
        ),
    ]
