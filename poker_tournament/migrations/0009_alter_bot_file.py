# Generated by Django 5.1.5 on 2025-01-26 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poker_tournament', '0008_alter_bot_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bot',
            name='file',
            field=models.FileField(max_length=5000, upload_to='static/bots/'),
        ),
    ]
