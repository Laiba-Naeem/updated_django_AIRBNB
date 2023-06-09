# Generated by Django 4.2 on 2023-05-15 13:39

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Hotel",
            fields=[
                ("hotel_id", models.IntegerField(primary_key=True, serialize=False)),
                ("hotel_name", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "hotel_location",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("bed_rooms", models.CharField(blank=True, max_length=50, null=True)),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
            ],
        ),
    ]
