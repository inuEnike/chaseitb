# Generated by Django 5.0.2 on 2024-02-18 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0010_deposit'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit',
            name='currency',
            field=models.CharField(default='$', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='crypto_balance',
            field=models.CharField(default='0', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='crypto_expense',
            field=models.CharField(default='0', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='crypto_income',
            field=models.CharField(default='0', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='main_balance',
            field=models.CharField(default='0', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='main_expense',
            field=models.CharField(default='0', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='main_income',
            field=models.CharField(default='0', max_length=200, null=True),
        ),
    ]