# Generated by Django 2.1.2 on 2018-11-08 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0008_remove_comment_seller_note_being_reviewed'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='product_id',
            field=models.IntegerField(default=0),
        ),
    ]
