# Generated by Django 4.0.2 on 2022-03-12 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('goal', models.IntegerField()),
                ('image', models.URLField()),
                ('is_open', models.BooleanField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('owner', models.CharField(max_length=200)),
            ],
        ),
    ]
