# Generated by Django 2.0 on 2019-12-18 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default=' ', max_length=200)),
                ('product_desc', models.TextField(blank=True, max_length=128)),
                ('product_slide_deck', models.FileField(blank=True, null=True, upload_to='slidedeck/')),
                ('scoping_document', models.FileField(blank=True, null=True, upload_to='scopingdoc/')),
                ('POC_SOW', models.FileField(blank=True, null=True, upload_to='POC_SOW/')),
                ('competitive_information', models.FileField(blank=True, null=True, upload_to='competitiveinfo/')),
                ('datasheet', models.FileField(blank=True, null=True, upload_to='datasheet/')),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technology_name', models.CharField(max_length=200)),
                ('technology_desc', models.TextField(blank=True, max_length=128)),
                ('domain', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='security.Domain')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='technology',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='security.Technology'),
        ),
    ]