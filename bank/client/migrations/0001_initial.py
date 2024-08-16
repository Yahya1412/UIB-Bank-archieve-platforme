# Generated by Django 5.0.4 on 2024-05-01 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ident', models.CharField(max_length=255)),
                ('nom', models.TextField()),
                ('prenom', models.TextField()),
                ('adresse', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('num_tel', models.PositiveIntegerField(null=True)),
                ('genre', models.TextField(blank=True, max_length=266, null=True)),
                ('nationalité', models.TextField(blank=True, max_length=266, null=True)),
                ('profession', models.TextField(blank=True, max_length=266, null=True)),
                ('statut_mat', models.TextField(blank=True, max_length=266, null=True)),
                ('nbr_per', models.PositiveIntegerField(null=True)),
                ('revenue_annuel', models.FloatField(null=True)),
                ('date_naissance', models.DateField()),
            ],
            options={
                'ordering': ['-date_naissance'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Nationalité',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Nbr_per',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Statut_mat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
