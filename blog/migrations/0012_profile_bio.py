# Generated by Django 3.1.5 on 2021-03-05 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='This is my bio'),
            preserve_default=False,
        ),
    ]
