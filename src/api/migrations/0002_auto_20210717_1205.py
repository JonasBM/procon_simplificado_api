# Generated by Django 3.2.5 on 2021-07-17 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipo_de_situacao',
            name='descricao',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tipo_de_situacao',
            name='css_cor',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
    ]
