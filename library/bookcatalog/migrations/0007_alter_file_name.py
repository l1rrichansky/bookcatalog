# Generated by Django 4.1.2 on 2022-10-20 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookcatalog', '0006_file_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
