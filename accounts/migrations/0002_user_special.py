# Generated by Django 4.1 on 2022-09-12 02:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='special',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='special until '),
        ),
    ]