# Generated by Django 4.1.1 on 2023-07-19 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_snippet_user_alter_snippet_lang'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='private',
            field=models.BooleanField(default=True),
        ),
    ]
