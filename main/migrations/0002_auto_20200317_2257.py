# Generated by Django 3.0.2 on 2020-03-17 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ner_form',
            name='txt',
            field=models.FileField(null=True, upload_to='path_and_rename'),
        ),
    ]
