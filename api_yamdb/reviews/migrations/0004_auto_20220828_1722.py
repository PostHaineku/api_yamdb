# Generated by Django 2.2.16 on 2022-08-28 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0003_auto_20220828_1702"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="title",
            name="genre",
        ),
        migrations.AddField(
            model_name="title",
            name="genre",
            field=models.ManyToManyField(
                related_name="genre_titles", to="reviews.Genre"
            ),
        ),
        migrations.AlterField(
            model_name="title",
            name="name",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="title",
            name="year",
            field=models.IntegerField(),
        ),
    ]
