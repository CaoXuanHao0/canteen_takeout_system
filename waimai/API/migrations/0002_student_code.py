# Generated by Django 2.2.4 on 2020-04-24 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='code',
            field=models.CharField(default=123456, max_length=100),
            preserve_default=False,
        ),
    ]
