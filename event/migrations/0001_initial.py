# Generated by Django 3.1.4 on 2021-01-20 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventReg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=255)),
                ('event_desc', models.CharField(max_length=255)),
                ('event_loc', models.CharField(max_length=100)),
                ('event_stdate', models.DateTimeField()),
                ('event_endate', models.DateTimeField()),
                ('event_deadline', models.DateTimeField()),
                ('event_poster', models.ImageField(default=None, upload_to='')),
                ('event_host_email', models.EmailField(max_length=254)),
                ('event_host_pwd', models.CharField(max_length=50)),
            ],
        ),
    ]
