# Generated by Django 4.0.4 on 2022-08-20 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0020_remove_mcqs_lesson_mcqs_course_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mcqs',
            name='iterability',
            field=models.PositiveIntegerField(default=9),
        ),
        migrations.AlterField(
            model_name='liveclassroom',
            name='number',
            field=models.PositiveIntegerField(default=130928),
        ),
    ]
