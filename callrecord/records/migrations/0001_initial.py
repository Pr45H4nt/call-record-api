# Generated by Django 4.1.5 on 2023-02-21 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CallRecord",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("from_number", models.PositiveIntegerField(max_length=15)),
                ("to_number", models.PositiveIntegerField(max_length=15)),
                ("start_time", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
