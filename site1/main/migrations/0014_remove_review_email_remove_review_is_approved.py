# Generated by Django 5.0.6 on 2024-05-17 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_review_is_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='email',
        ),
        migrations.RemoveField(
            model_name='review',
            name='is_approved',
        ),
    ]