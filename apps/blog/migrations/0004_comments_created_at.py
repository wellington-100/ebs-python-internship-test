# Generated by Django 4.2.14 on 2024-09-11 22:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_comments"),
    ]

    operations = [
        migrations.AddField(
            model_name="comments",
            name="created_at",
            field=models.DateField(auto_now_add=True, db_index=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
