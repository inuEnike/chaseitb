# Generated by Django 5.0.2 on 2024-02-19 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0018_transfer_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='bank',
            field=models.CharField(max_length=200, null=True),
        ),
    ]