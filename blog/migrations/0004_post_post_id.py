# Generated by Django 3.1.5 on 2021-01-15 14:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210115_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_id',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
