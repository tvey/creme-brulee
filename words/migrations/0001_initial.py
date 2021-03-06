# Generated by Django 3.2.9 on 2021-11-23 19:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Expression',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Выражение')),
            ],
            options={
                'verbose_name': 'Выражение',
                'verbose_name_plural': 'Выражения',
                'ordering': ['content'],
            },
        ),
        migrations.CreateModel(
            name='ExpressionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_type', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Тип выражений',
                'verbose_name_plural': 'Типы выражений',
            },
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=50, verbose_name='Слово')),
                ('num_r', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Количество *р* в слове')),
                ('part_of_speech', models.CharField(blank=True, choices=[('verb', 'глагол'), ('noun', 'существительное'), ('adjective ', 'прилагательное'), ('numeral ', 'числительное'), ('adverb', 'наречие'), ('participle ', 'причастие'), ('other ', 'другое')], max_length=20, null=True, verbose_name='Часть речи')),
                ('in_stressed', models.BooleanField(blank=True, null=True, verbose_name='*р* в ударном слоге')),
                ('hard_or_soft', models.CharField(blank=True, choices=[('soft', 'твёрдый'), ('hard', 'твёрдый')], max_length=20, null=True, verbose_name='Твёрдый или мягкий звук *р*')),
                ('num_syllables', models.PositiveSmallIntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3+')], null=True, verbose_name='Количество слогов')),
                ('difficulty', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'easy'), (1, 'medium'), (2, 'hard'), (3, 'extreme')], null=True, verbose_name='Сложность')),
                ('frequency', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('is_active', models.BooleanField(blank=True, default=True, null=True)),
            ],
            options={
                'verbose_name': 'Слово',
                'verbose_name_plural': 'Слова',
                'ordering': ['content'],
            },
        ),
        migrations.CreateModel(
            name='UserWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_selected', models.BooleanField(blank=True, help_text='Возможность добавить слово в избранное', null=True, verbose_name='Избранное')),
                ('is_disliked', models.BooleanField(blank=True, help_text='Возможность исключить слово', null=True, verbose_name='Не нравится')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='words.word', verbose_name='Слово')),
            ],
            options={
                'verbose_name': 'Избранное слово',
                'verbose_name_plural': 'Избранные слова',
            },
        ),
        migrations.CreateModel(
            name='UserExpression',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_selected', models.BooleanField(blank=True, help_text='Возможность добавить выражение в избранное', null=True, verbose_name='Избранное')),
                ('is_disliked', models.BooleanField(blank=True, help_text='Возможность исключить выражение', null=True, verbose_name='Не нравится')),
                ('expression', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='words.expression', verbose_name='Выражение')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Избранное выражение',
                'verbose_name_plural': 'Избранные выражения',
            },
        ),
        migrations.AddField(
            model_name='expression',
            name='e_type',
            field=models.ManyToManyField(to='words.ExpressionType', verbose_name='Тип выражения'),
        ),
        migrations.AddField(
            model_name='expression',
            name='words',
            field=models.ManyToManyField(related_name='e_words', to='words.Word', verbose_name='Слова в выражении'),
        ),
    ]
