# Generated by Django 3.1.4 on 2021-01-24 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_auto_20210123_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventreg',
            name='event_poster',
            field=models.ImageField(upload_to='eventPoster/'),
        ),
    ]
