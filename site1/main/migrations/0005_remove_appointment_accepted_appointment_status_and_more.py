# Generated by Django 5.0.6 on 2024-05-15 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_service_description_service_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='accepted',
        ),
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.CharField(default='Pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='service',
            field=models.CharField(max_length=100),
        ),
    ]
