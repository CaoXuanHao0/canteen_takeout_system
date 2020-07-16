# Generated by Django 3.0.3 on 2020-05-06 02:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20200506_0033'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='last_login',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='上次登录时间'),
            preserve_default=False,
        ),
    ]
