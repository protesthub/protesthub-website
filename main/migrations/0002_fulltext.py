# Generated by Django 2.2 on 2019-05-03 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            ('CREATE FULLTEXT INDEX search_index ON main_demo (title,adress,organizer,description)',),
            ('DROP INDEX search_index on main_demo',)
        ),
    ]
