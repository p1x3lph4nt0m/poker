# Generated by Django 5.1.5 on 2025-01-22 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poker_tournament', '0002_bot_match_testbot_testmatch_round'),
    ]

    operations = [
        migrations.AddField(
            model_name='testbot',
            name='chips_won',
            field=models.IntegerField(default=0),
        ),
    ]
