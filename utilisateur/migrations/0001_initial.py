# Generated by Django 3.1.5 on 2021-01-16 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prospects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='Email')),
                ('nom', models.CharField(max_length=255, verbose_name='Nom')),
                ('prenom', models.CharField(max_length=255, verbose_name='prenom')),
                ('numero1', models.IntegerField(verbose_name='Numéro de téléphone')),
                ('numero2', models.IntegerField(verbose_name='Numéro whatsapp')),
                ('lieu', models.CharField(max_length=255, verbose_name='lieu de naissance')),
                ('sexe', models.CharField(max_length=255, verbose_name='Sexe')),
                ('filiere', models.CharField(max_length=255, verbose_name='Filière')),
                ('diplome', models.CharField(max_length=255, verbose_name='Diplôme')),
            ],
        ),
        migrations.CreateModel(
            name='Delegate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('delegue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utilisateur.prospects')),
            ],
        ),
    ]
