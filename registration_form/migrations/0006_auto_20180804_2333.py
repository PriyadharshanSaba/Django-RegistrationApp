# Generated by Django 2.0.7 on 2018-08-04 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_form', '0005_auto_20180804_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='expr',
            field=models.CharField(choices=[('beg', 'Beginner (0 - 5 runs)'), ('inter', 'Intermediate ( 6 - 10 runs)'), ('pro', 'Professional (10+ runs)')], max_length=100, null=True),
        ),
    ]