# Generated by Django 3.1.5 on 2021-03-06 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20210306_0403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(default='This is blog post'),
        ),
    ]
