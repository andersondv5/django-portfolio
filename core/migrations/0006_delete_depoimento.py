# Generated by Django 5.2 on 2025-05-02 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_depoimento_delete_blogpost'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Depoimento',
        ),
    ]
