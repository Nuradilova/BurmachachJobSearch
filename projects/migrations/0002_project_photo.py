# Generated by Django 4.1.6 on 2023-02-22 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="photo",
            field=models.ImageField(blank=True, default="", null=True, upload_to=""),
        ),
    ]
