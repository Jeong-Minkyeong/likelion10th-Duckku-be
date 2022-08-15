# Generated by Django 4.1 on 2022-08-13 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music_name', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='album_image',
            field=models.ImageField(blank=True, null=True, upload_to='sang_album_img'),
        ),
        migrations.AddField(
            model_name='album',
            name='price_with_ticket',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='album',
            name='price_without_ticket',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='albumfrime',
            name='album_image',
            field=models.ImageField(blank=True, null=True, upload_to='buy_album_img'),
        ),
        migrations.AddField(
            model_name='albumfrime',
            name='buyNumber',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='artist',
            name='agency',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='artist',
            name='artist_image',
            field=models.ImageField(blank=True, null=True, upload_to='artist_img'),
        ),
        migrations.AddField(
            model_name='photocard',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='photocardfrime',
            name='QR_image',
            field=models.ImageField(blank=True, null=True, upload_to='QR_image'),
        ),
        migrations.AddField(
            model_name='photocardfrime',
            name='QR_used',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='photocardfrime',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='photocardfrime',
            name='register_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='photocard',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='sang_photo_card_img'),
        ),
        migrations.AlterField(
            model_name='photocardfrime',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='buy_photo_card_img'),
        ),
        migrations.AddField(
            model_name='album',
            name='music_list',
            field=models.ManyToManyField(blank=True, related_name='sang_music_list', to='album.music'),
        ),
        migrations.AddField(
            model_name='albumfrime',
            name='music_list',
            field=models.ManyToManyField(blank=True, related_name='my_music_list', to='album.music'),
        ),
    ]
