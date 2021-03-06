# Generated by Django 3.1.4 on 2020-12-11 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreditCardNumber', models.CharField(max_length=12)),
                ('CardHolder', models.CharField(max_length=50)),
                ('ExpirationDate', models.DateField()),
                ('SecurityCode', models.CharField(max_length=3)),
                ('Amount', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
