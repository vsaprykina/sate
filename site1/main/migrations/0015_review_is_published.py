# Generated by Django 5.0.6 on 2024-05-17 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_remove_review_email_remove_review_is_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]