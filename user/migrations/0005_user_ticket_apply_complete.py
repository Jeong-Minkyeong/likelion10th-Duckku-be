# Generated by Django 4.1 on 2022-08-13 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_rename_userbuyalbumlist_user_userbuyalbum_type_list_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ticket_apply_complete',
            field=models.BooleanField(default=False, null=True),
        ),
    ]