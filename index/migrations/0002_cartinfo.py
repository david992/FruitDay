# Generated by Django 3.0.5 on 2020-05-03 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ccount', models.IntegerField(db_column='ccount')),
                ('goods', models.ForeignKey(db_column='goods_id', on_delete=django.db.models.deletion.CASCADE, to='index.Goods')),
                ('user', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='index.User')),
            ],
            options={
                'db_table': 'cart_info',
            },
        ),
    ]
