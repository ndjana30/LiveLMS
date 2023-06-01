# Generated by Django 4.0.4 on 2022-08-21 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0027_alter_liveclassroom_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liveclassroom',
            name='number',
            field=models.PositiveIntegerField(default=341529),
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=250)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizes', to='school.course')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentence', models.TextField(max_length=255)),
                ('a', models.TextField(max_length=255)),
                ('b', models.TextField(max_length=255)),
                ('c', models.TextField(max_length=255)),
                ('d', models.TextField(max_length=255)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='school.quiz')),
            ],
        ),
    ]