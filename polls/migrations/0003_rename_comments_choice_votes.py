# Generated by Django 4.1.5 on 2023-02-12 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_remove_choice_votes_choice_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='comments',
            new_name='votes',
        ),
    ]
