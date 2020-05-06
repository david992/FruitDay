# Generated by Django 3.0.5 on 2020-05-03 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='类型标题')),
                ('picture', models.ImageField(null=True, upload_to='static/upload/goodstype', verbose_name='类型图片')),
                ('desc', models.TextField(verbose_name='类型描述')),
            ],
            options={
                'verbose_name': '商品类型',
                'verbose_name_plural': '商品类型',
                'db_table': 'goods_type',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uphone', models.CharField(max_length=11, verbose_name='联系方式')),
                ('upwd', models.CharField(max_length=20, verbose_name='密码')),
                ('uname', models.CharField(max_length=30, verbose_name='用户名')),
                ('uemail', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('isActive', models.BooleanField(default=True, verbose_name='活跃状态')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='商品名称')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='商品价格')),
                ('spec', models.CharField(max_length=20, verbose_name='商品规格')),
                ('picture', models.ImageField(null=True, upload_to='static/upload/goods', verbose_name='商品图片')),
                ('isActive', models.BooleanField(default=True, verbose_name='是否上架')),
                ('goodsType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.GoodsType', verbose_name='商品类型')),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
                'db_table': 'goods',
            },
        ),
    ]
