# Generated by Django 5.1.1 on 2024-09-11 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("restaurants", "0007_menu_votes"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Vote",
        ),
    ]
