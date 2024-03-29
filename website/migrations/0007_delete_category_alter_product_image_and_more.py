# Generated by Django 4.2.4 on 2023-12-06 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_alter_product_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='category',
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='website/static/upload_images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
