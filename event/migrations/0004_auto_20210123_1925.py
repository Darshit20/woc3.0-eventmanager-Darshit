# Generated by Django 3.1.4 on 2021-01-23 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20210123_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventreg',
            name='event_deadline',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='eventreg',
            name='event_endate',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='eventreg',
            name='event_stdate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
