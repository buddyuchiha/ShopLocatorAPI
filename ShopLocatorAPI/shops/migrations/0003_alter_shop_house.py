# Generated by Django 5.2.3 on 2025-07-01 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0002_alter_shop_time_close_alter_shop_time_open'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='house',
            field=models.SlugField(max_length=255),
        ),
    ]
