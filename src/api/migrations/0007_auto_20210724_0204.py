# Generated by Django 3.2.5 on 2021-07-24 05:04

from django.db import migrations
from django.contrib.postgres.operations import TrigramExtension
from django.contrib.postgres.operations import UnaccentExtension


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0006_alter_situcacao_data"),
    ]

    operations = [UnaccentExtension(), TrigramExtension()]
