# Generated by Django 2.2.8 on 2019-12-25 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0011_auto_20191225_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='locked',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
