# Generated by Django 4.0.6 on 2022-08-09 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='projectfeatures',
            field=models.TextField(),
        ),
    ]