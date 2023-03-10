# Generated by Django 4.1.5 on 2023-01-07 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leaderboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('quiz_name', models.CharField(max_length=200)),
                ('total', models.CharField(max_length=200)),
                ('correct', models.CharField(max_length=200)),
                ('incorrect', models.CharField(max_length=200)),
                ('percentage', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Quiz_Leaderboard',
            },
        ),
        migrations.CreateModel(
            name='QuizName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'QuizName',
            },
        ),
        migrations.CreateModel(
            name='QuestionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('option1', models.CharField(max_length=200)),
                ('option2', models.CharField(max_length=200)),
                ('option3', models.CharField(max_length=200)),
                ('option4', models.CharField(max_length=200)),
                ('answer', models.CharField(max_length=200)),
                ('hint', models.CharField(max_length=500)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz_app.quizname')),
            ],
            options={
                'db_table': 'QuestionModel',
            },
        ),
    ]
