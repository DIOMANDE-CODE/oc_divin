# Generated by Django 3.1.5 on 2021-01-15 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0002_delegate'),
    ]

    operations = [
        migrations.AddField(
            model_name='delegate',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]