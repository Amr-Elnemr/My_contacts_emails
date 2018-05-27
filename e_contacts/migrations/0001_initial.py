# Generated by Django 2.0.5 on 2018-05-26 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(error_messages={'required': 'Please provide your email address.', 'unique': 'An account with this email exist.'}, max_length=254, unique=True)),
            ],
        ),
    ]
