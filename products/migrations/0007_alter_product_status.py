# Generated by Django 4.1 on 2022-09-12 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('d', 'draft'), ('p', 'publish')], default='d', max_length=1),
        ),
    ]
