# Generated by Django 4.0.4 on 2022-07-30 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0014_remove_quizz_name_remove_quizz_no_questions_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quizz',
            old_name='op1',
            new_name='A',
        ),
        migrations.RenameField(
            model_name='quizz',
            old_name='op2',
            new_name='B',
        ),
        migrations.RenameField(
            model_name='quizz',
            old_name='op3',
            new_name='C',
        ),
        migrations.RenameField(
            model_name='quizz',
            old_name='op4',
            new_name='D',
        ),
        migrations.AlterField(
            model_name='liveclassroom',
            name='number',
            field=models.PositiveIntegerField(default=735157),
        ),
    ]