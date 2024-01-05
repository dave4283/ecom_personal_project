
from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_review_createdat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='commment',
            new_name='comment',
        ),
        # You can keep the createdAt field by not removing it
        # migrations.RemoveField(
        #     model_name='review',
        #     name='createdAt',
        # ),
    ]