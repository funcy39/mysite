# Generated by Django 4.1.5 on 2023-02-12 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funnymanga', '0003_alter_comment_comment_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_counts',
            new_name='comments',
        ),
    ]
