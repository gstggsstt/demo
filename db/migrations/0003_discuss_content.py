# Generated by Django 2.2.8 on 2019-12-23 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_auto_20191223_0034'),
    ]

    operations = [
        migrations.AddField(
            model_name='discuss',
            name='content',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
