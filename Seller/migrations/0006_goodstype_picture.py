# Generated by Django 2.1.8 on 2019-09-10 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0005_auto_20190909_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodstype',
            name='picture',
            field=models.ImageField(default='', upload_to='seller/images'),
            preserve_default=False,
        ),
    ]
