# Generated by Django 3.1.6 on 2021-03-14 14:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0007_auto_20210314_1418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='teacher',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]