# Generated by Django 4.0.4 on 2022-08-21 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0025_remove_mcqs_name_alter_liveclassroom_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liveclassroom',
            name='number',
            field=models.PositiveIntegerField(default=43634),
        ),
        migrations.DeleteModel(
            name='MCQS',
        ),
    ]