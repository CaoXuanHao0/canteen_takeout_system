# Generated by Django 2.2.2 on 2020-05-09 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20200508_0932'),
    ]

    operations = [
        migrations.DeleteModel(
            name='deliveryman',
        ),
        migrations.AddField(
            model_name='student_contact',
            name='is_default',
            field=models.BooleanField(default=True, verbose_name='默认联系方式'),
            preserve_default=False,
        ),
    ]
