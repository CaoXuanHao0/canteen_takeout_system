# Generated by Django 3.0.5 on 2020-05-08 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diancan', '0011_auto_20200508_0851'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='grade_choice',
            field=models.CharField(default='5', max_length=10),
        ),
    ]