# Generated by Django 4.1 on 2022-08-14 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_music_album_album_image_album_price_with_ticket_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='purchased_count',
            field=models.IntegerField(default=0, null=True),
        ),
    ]