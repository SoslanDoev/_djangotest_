# Generated by Django 5.0.6 on 2024-05-27 22:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('surname', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=100, verbose_name='Отчество')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
                'ordering': ['surname', 'name', 'patronymic'],
            },
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Дисциплина',
                'verbose_name_plural': 'Дисциплины',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('surname', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=100, verbose_name='Отчество')),
                ('block', models.BooleanField(default=False, verbose_name='Заблокирован')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Почта')),
                ('login', models.CharField(max_length=100, unique=True, verbose_name='Логин')),
                ('password', models.CharField(max_length=100, verbose_name='Пароль')),
                ('token', models.CharField(blank=True, max_length=255, unique=True, verbose_name='Токен')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.group', verbose_name='Группа')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
                'ordering': ['surname', 'name', 'patronymic'],
            },
        ),
        migrations.CreateModel(
            name='Testing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.author', verbose_name='Автор')),
                ('discipline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.discipline', verbose_name='Дисциплина')),
            ],
            options={
                'verbose_name': 'Тестирование',
                'verbose_name_plural': 'Тестирования',
                'ordering': ['discipline', 'title'],
            },
        ),
        migrations.CreateModel(
            name='ScheduleTesting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_start', models.DateTimeField(verbose_name='Начало тестирования')),
                ('time_end', models.DateTimeField(verbose_name='Конец тестирования')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.group', verbose_name='Группа')),
                ('testing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.testing', verbose_name='Тестирование')),
            ],
            options={
                'verbose_name': 'Настройка тестирования',
                'verbose_name_plural': 'Настройки тестирования',
                'ordering': ['testing', 'time_start'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Текст вопроса')),
                ('ball', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Балл за правильный ответ')),
                ('testing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.testing', verbose_name='Тестирование')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Текст варианта ответа')),
                ('is_correct', models.BooleanField(default=False, verbose_name='Правильный ответ')),
                ('ball', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Балл за правильный ответ')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.question', verbose_name='Вопрос')),
            ],
            options={
                'verbose_name': 'Вариант ответа',
                'verbose_name_plural': 'Варианты ответов',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open_text_response', models.TextField(blank=True, null=True, verbose_name='Открытый ответ')),
                ('host', models.CharField(max_length=255, verbose_name='Хост')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.student', verbose_name='Студент')),
                ('variant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.variant', verbose_name='Вариант')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
                'ordering': ['student'],
            },
        ),
    ]
