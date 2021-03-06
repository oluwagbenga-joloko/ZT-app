# Generated by Django 3.0.6 on 2020-05-05 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TempMeasurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(null=True)),
                ('temperature', models.FloatField(null=True)),
                ('duration', models.DurationField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
