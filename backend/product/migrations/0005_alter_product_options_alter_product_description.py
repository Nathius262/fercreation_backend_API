# Generated by Django 4.0.4 on 2023-01-14 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_date_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['date_created']},
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, verbose_name='describe_product'),
        ),
    ]
