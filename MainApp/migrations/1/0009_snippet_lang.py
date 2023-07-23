# Generated by Django 4.1.1 on 2023-07-23 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0008_remove_snippet_lang'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='lang',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='MainApp.language'),
        ),
    ]