# Generated by Django 2.2.13 on 2021-04-09 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0015_domainaddress'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeletedDomainAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_hash', models.CharField(db_index=True, max_length=64)),
                ('domain_hash', models.CharField(db_index=True, max_length=64)),
                ('num_forwarded', models.PositiveSmallIntegerField(default=0)),
                ('num_blocked', models.PositiveSmallIntegerField(default=0)),
                ('num_spam', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
    ]
