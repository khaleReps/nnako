# Generated by Django 4.2.3 on 2023-07-31 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='username',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]