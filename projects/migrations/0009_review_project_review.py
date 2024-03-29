# Generated by Django 4.1.6 on 2023-03-25 06:24

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0008_remove_project_review_delete_review"),
    ]

    operations = [
        migrations.CreateModel(
            name="Review",
            fields=[
                ("content", models.CharField(max_length=300)),
                (
                    "vote",
                    models.CharField(
                        blank=True,
                        choices=[("up", "Up Vote"), ("down", "Down Vote")],
                        max_length=20,
                        null=True,
                    ),
                ),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="project",
            name="review",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="projects.review",
            ),
        ),
    ]
