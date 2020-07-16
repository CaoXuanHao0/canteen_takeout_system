# Generated by Django 2.2.2 on 2020-05-08 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diancan', '0008_auto_20200506_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='canteen_name',
            field=models.CharField(choices=[('xinbei', '新北区餐厅'), ('heyi', '合一楼餐厅'), ('xuer', '学二餐厅')], default=1, max_length=10, verbose_name='订单餐厅'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='OrderID',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='订单编号'),
        ),
        migrations.CreateModel(
            name='dishes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='菜品名称')),
                ('num', models.IntegerField(verbose_name='订购数量')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='菜品总价')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_dishes', to='diancan.order', verbose_name='订单编号')),
            ],
        ),
    ]