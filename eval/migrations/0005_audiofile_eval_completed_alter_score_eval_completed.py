# Generated by Django 4.1.4 on 2023-04-30 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eval", "0004_remove_eval_item_eval_completed"),
    ]

    operations = [
        migrations.AddField(
            model_name="audiofile",
            name="eval_completed",
            field=models.CharField(
                default="미완료", max_length=10, verbose_name="평가 완료 여부"
            ),
        ),
        migrations.AlterField(
            model_name="score",
            name="eval_completed",
            field=models.BooleanField(default="미완료", verbose_name="평가 완료 여부"),
        ),
    ]
