# Generated by Django 5.0.6 on 2024-06-04 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=100)),
                ('phone_numbers', models.TextField(help_text='Separate multiple phone numbers with a comma')),
            ],
        ),
    ]
