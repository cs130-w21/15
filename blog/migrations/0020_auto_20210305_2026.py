# Generated by Django 3.1.5 on 2021-03-06 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20210306_0413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='snippet',
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(default=''),
        ),
    ]
