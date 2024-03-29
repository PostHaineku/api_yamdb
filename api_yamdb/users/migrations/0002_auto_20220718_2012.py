# Generated by Django 2.2.16 on 2022-07-18 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                blank=True,
                choices=[
                    ("admin", "admin"),
                    ("moderator", "moderator"),
                    ("user", "user"),
                ],
                default="user",
                max_length=10,
                null=True,
            ),
        ),
    ]
