# Generated by Django 4.0.8 on 2023-11-24 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('streaming', '0009_alter_episode_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='episode',
            options={'ordering': ['season', 'episode_number']},
        ),
    ]
