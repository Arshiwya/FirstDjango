# Generated by Django 4.1 on 2022-08-21 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(related_name='product', to='products.category', verbose_name='دسته بندی ها'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.BigIntegerField(null=True),
        ),
    ]
