# Generated by Django 4.2.4 on 2023-12-06 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_remove_product_price_product_cut_price_product_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/upload_images/'),
        ),
    ]
