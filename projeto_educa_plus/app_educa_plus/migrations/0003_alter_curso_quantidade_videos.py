# Generated by Django 5.1.1 on 2024-12-09 23:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_educa_plus", "0002_curso"),
    ]

    operations = [
        migrations.AlterField(
            model_name="curso",
            name="quantidade_videos",
            field=models.IntegerField(null=True),
        ),
    ]