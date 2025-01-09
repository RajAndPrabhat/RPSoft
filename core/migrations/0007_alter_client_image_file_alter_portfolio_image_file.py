# Generated by Django 5.1.4 on 2025-01-09 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_client_portfolio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='image_file',
            field=models.ImageField(upload_to='clients'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image_file',
            field=models.ImageField(upload_to='portfolios'),
        ),
    ]
