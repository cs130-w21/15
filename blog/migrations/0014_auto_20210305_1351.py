# Generated by Django 3.1.5 on 2021-03-05 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile'),
        ),
    ]
