# Generated by Django 5.0.2 on 2024-02-19 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0014_remove_pict_profile_pic_card_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='profile_pic',
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='avater.png', null=True, upload_to=''),
        ),
        migrations.DeleteModel(
            name='Pict',
        ),
    ]
