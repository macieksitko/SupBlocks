# Generated by Django 3.0.3 on 2020-11-09 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='nonce',
            field=models.IntegerField(default=4460391),
        ),
    ]