# Generated by Django 2.1.8 on 2019-09-19 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buyer', '0002_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='goods_total_price',
            field=models.FloatField(default=1),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='order_status',
            field=models.IntegerField(default=0),
        ),
    ]
