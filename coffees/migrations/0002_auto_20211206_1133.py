# Generated by Django 3.2.9 on 2021-12-06 03:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('coffees', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coffee',
            options={'verbose_name': '咖啡', 'verbose_name_plural': '咖啡'},
        ),
        migrations.AlterModelOptions(
            name='grinding',
            options={'verbose_name': '磨豆方式', 'verbose_name_plural': '磨豆方式'},
        ),
        migrations.AlterModelOptions(
            name='mainprocessing',
            options={'verbose_name': '主要處理法', 'verbose_name_plural': '主要處理法'},
        ),
        migrations.AlterModelOptions(
            name='originplace',
            options={'verbose_name': '產地', 'verbose_name_plural': '產地'},
        ),
        migrations.AddField(
            model_name='coffee',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 12, 6, 3, 31, 42, 421860, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coffee',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='grinding',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 12, 6, 3, 33, 30, 215166, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grinding',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
