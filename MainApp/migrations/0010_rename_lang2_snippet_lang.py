# Generated by Django 4.1.1 on 2023-07-23 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0009_remove_snippet_lang'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snippet',
            old_name='lang2',
            new_name='lang',
        ),
    ]