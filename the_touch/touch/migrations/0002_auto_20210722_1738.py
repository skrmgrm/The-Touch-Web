# Generated by Django 3.1.7 on 2021-07-22 09:38

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('touch', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='touch',
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
    ]
