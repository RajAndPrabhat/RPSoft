# Generated by Django 5.1.4 on 2025-01-09 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_sliders'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=500)),
                ('image_file', models.ImageField(upload_to='sliders')),
            ],
        ),
        migrations.RenameModel(
            old_name='Services',
            new_name='Service',
        ),
        migrations.RenameModel(
            old_name='Sliders',
            new_name='Slider',
        ),
    ]
