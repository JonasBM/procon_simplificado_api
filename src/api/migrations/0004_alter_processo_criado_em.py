# Generated by Django 3.2.5 on 2021-07-22 14:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210721_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processo',
            name='criado_em',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
