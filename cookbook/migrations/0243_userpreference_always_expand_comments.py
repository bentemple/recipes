from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0242_space_household_setup_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpreference',
            name='always_expand_comments',
            field=models.BooleanField(default=True),
        ),
    ]
