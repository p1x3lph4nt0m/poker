# Generated by Django 5.1.5 on 2025-01-23 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poker_tournament', '0006_alter_match_rounds_data_alter_round_replay_data_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bot',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='bot',
            name='path',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='match',
            name='winner',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='round',
            name='winner',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='testbot',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='testmatch',
            name='opponent_name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='testmatch',
            name='winner',
            field=models.TextField(),
        ),
    ]
