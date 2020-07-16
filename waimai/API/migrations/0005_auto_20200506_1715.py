# Generated by Django 3.0.3 on 2020-05-06 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_student_last_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='dnum',
        ),
        migrations.RemoveField(
            model_name='student',
            name='tele',
        ),
        migrations.CreateModel(
            name='student_contact',
            fields=[
                ('contact_ID', models.IntegerField(auto_created=True, editable=False, primary_key=True, serialize=False, verbose_name='联系信息编号')),
                ('telephone_num', models.CharField(max_length=11, verbose_name='电话号码')),
                ('destination', models.CharField(choices=[('1', '1公寓'), ('2', '2公寓'), ('3', '3公寓'), ('4', '4公寓'), ('5', '5公寓'), ('6', '6公寓'), ('7', '7公寓'), ('8', '8公寓'), ('9', '9公寓'), ('10', '10公寓'), ('11', '11公寓'), ('12', '12公寓'), ('13', '13公寓'), ('14', '14公寓'), ('15', '15公寓'), ('16', '16公寓'), ('17', '17公寓'), ('18', '18公寓'), ('19', '19公寓'), ('20', '20公寓'), ('21', '21公寓'), ('22', '22公寓'), ('23', '23公寓'), ('24', '24公寓'), ('25', '25公寓'), ('26', '26公寓'), ('27', '27公寓'), ('28', '28公寓'), ('29', '29公寓'), ('30', '30公寓'), ('31', '新主楼'), ('32', '大运村')], max_length=2, verbose_name='送货地点')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_contact', to='login.student', verbose_name='学生学号')),
            ],
        ),
    ]
