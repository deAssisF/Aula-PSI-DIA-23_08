# Generated by Django 5.0.7 on 2024-08-23 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=20)),
                ('prazo', models.DateField()),
            ],
        ),
    ]
