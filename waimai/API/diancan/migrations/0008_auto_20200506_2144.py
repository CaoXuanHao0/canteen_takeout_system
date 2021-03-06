# Generated by Django 2.2.2 on 2020-05-06 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diancan', '0007_auto_20200506_1754'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='heyi',
            options={'verbose_name': '合一楼食堂', 'verbose_name_plural': '合一楼食堂'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': '全部订单', 'verbose_name_plural': '全部订单'},
        ),
        migrations.AlterModelOptions(
            name='xinbei',
            options={'verbose_name': '新北区食堂', 'verbose_name_plural': '新北区食堂'},
        ),
        migrations.AlterModelOptions(
            name='xuer',
            options={'verbose_name': '学二食堂', 'verbose_name_plural': '学二食堂'},
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('ordered', '已下单'), ('processing', '配送中'), ('paying', '待付款'), ('canceled', '已取消'), ('completed', '已完成')], default=1, max_length=10, verbose_name='订单状态'),
            preserve_default=False,
        ),
    ]
