# Generated by Django 4.0.3 on 2022-04-17 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detaform',
            name='emali',
            field=models.EmailField(max_length=254),
        ),
    ]