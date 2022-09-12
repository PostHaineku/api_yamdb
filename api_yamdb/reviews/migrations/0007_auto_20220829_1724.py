# Generated by Django 2.2.16 on 2022-08-29 14:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0006_comment_title"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="review",
            name="only_one_review",
        ),
        migrations.AlterField(
            model_name="review",
            name="score",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(10),
                ]
            ),
        ),
    ]