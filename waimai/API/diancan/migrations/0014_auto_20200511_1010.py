# Generated by Django 2.2.2 on 2020-05-11 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diancan', '0013_auto_20200509_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='heyi',
            name='image_source',
            field=models.ImageField(default='media/image/heyi/学二餐厅.jpg', upload_to='', verbose_name='菜品照片原图'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='xinbei',
            name='image_source',
            field=models.ImageField(default='media/image/heyi/学二餐厅.jpg', upload_to='', verbose_name='菜品照片原图'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='xuer',
            name='image_source',
            field=models.ImageField(default='', upload_to='', verbose_name='菜品照片原图'),
            preserve_default=False,
        ),
    ]
