# Generated by Django 5.2 on 2025-04-29 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_projeto'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='descricao',
            field=models.TextField(default=''),
        ),
    ]
