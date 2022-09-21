# Generated by Django 4.1 on 2022-09-17 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexform', '0007_friendlist_alter_relationship_receiver_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('brand', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.PositiveIntegerField()),
            ],
        ),
    ]
