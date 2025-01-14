# Generated by Django 4.1.1 on 2023-07-23 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0006_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=32)),
                ('shot_name', models.CharField(max_length=8)),
            ],
        ),
        migrations.AlterField(
            model_name='snippet',
            name='lang',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='MainApp.language'),
        ),
    ]
