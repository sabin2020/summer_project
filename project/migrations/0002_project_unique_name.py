# Generated by Django 3.1.6 on 2021-03-08 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='unique_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
