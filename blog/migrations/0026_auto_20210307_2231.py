# Generated by Django 3.1.7 on 2021-03-07 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_merge_20210307_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='I have not written anything about myself yet', null=True),
        ),
    ]
