# Generated by Django 2.2.8 on 2019-12-25 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0007_section_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='ver_number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]