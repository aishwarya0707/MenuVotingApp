# Generated by Django 5.1.1 on 2024-09-06 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('cuisine_type', models.CharField(blank=True, max_length=100, null=True)),
                ('opening_hours', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
