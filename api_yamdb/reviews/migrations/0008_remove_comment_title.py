# Generated by Django 2.2.16 on 2022-08-30 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0007_auto_20220829_1724"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="title",
        ),
    ]
