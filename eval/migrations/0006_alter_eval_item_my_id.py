# Generated by Django 4.1.4 on 2023-05-12 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eval", "0005_audiofile_eval_completed_alter_score_eval_completed"),
    ]

    operations = [
        migrations.AlterField(
            model_name="eval_item",
            name="my_id",
            field=models.CharField(blank=True, max_length=200, verbose_name="my_id"),
        ),
    ]
