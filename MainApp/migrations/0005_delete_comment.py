# Generated by Django 4.1.1 on 2023-07-20 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0004_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]