# Generated by Django 5.0.6 on 2024-07-18 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_listing', '0002_name_pokedex_entry'),
    ]

    operations = [
        migrations.AddField(
            model_name='name',
            name='url',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
