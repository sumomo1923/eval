# Generated by Django 4.1.7 on 2023-04-07 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eval", "0004_remove_eval_item_my_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="eval_item",
            name="my_id",
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
