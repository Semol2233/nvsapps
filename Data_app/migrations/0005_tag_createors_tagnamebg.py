# Generated by Django 2.2.5 on 2020-07-24 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data_app', '0004_auto_20200724_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag_createors',
            name='tagNameBG',
            field=models.CharField(default='success', max_length=100),
        ),
    ]
