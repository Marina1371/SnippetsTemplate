# Generated by Django 4.1.1 on 2023-07-23 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0007_language_alter_snippet_lang'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snippet',
            name='lang',
        ),
    ]
