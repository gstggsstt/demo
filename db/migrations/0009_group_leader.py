# Generated by Django 2.2.8 on 2019-12-25 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0008_group_ver_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='leader',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='leader', to='db.Student'),
            preserve_default=False,
        ),
    ]