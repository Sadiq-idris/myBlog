# Generated by Django 4.1.5 on 2023-05-19 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0004_rename_user_comment_comment_username"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="Comment_username",
            new_name="comment_username",
        ),
    ]
