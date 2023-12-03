# Generated by Django 4.0.8 on 2023-11-19 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streaming', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(related_name='movies', to='streaming.genre'),
        ),
        migrations.AddField(
            model_name='series',
            name='genres',
            field=models.ManyToManyField(related_name='series', to='streaming.genre'),
        ),
    ]
