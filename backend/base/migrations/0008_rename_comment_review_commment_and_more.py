# Generated by Django 4.2.4 on 2023-12-27 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_review_createdat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='comment',
            new_name='commment',
        ),
        migrations.RemoveField(
            model_name='review',
            name='createdAt',
        ),
    ]
