from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Word(models.Model):
    """Слово, одна единица."""

    DIFFICULTY_CHOICES = [
        (0, 'easy'),
        (1, 'medium'),
        (2, 'hard'),
        (3, 'extreme'),
    ]
    POS_CHOICES = [
        ('verb', 'глагол'),
        ('noun', 'существительное'),
        ('adjective ', 'прилагательное'),
        ('numeral ', 'числительное'),
        ('adverb', 'наречие'),
        ('participle ', 'причастие'),
        ('other ', 'другое'),
    ]
    NUM_SYLLABLES = [
        (1, '1'),
        (2, '2'),
        (3, '3+'),
    ]

    word = models.CharField('Слово', max_length=50)
    num_r = models.PositiveSmallIntegerField(
        'Количество *р* в слове',
        blank=True,
        null=True,
    )
    part_of_speech = models.CharField(
        'Часть речи',
        max_length=20,
        choices=POS_CHOICES,
        blank=True,
        null=True,
    )
    in_stressed = models.BooleanField(
        '*р* в ударном слоге',
        blank=True,
        null=True,
    )
    hard_or_soft = models.CharField(
        'Твёрдый или мягкий звук *р*',
        max_length=20,
        choices=[('soft', 'твёрдый'), ('hard', 'твёрдый')],
        blank=True,
        null=True,
    )
    num_syllables = models.PositiveSmallIntegerField(
        'Количество слогов',
        choices=NUM_SYLLABLES,
        blank=True,
        null=True,
    )
    difficulty = models.PositiveSmallIntegerField(
        'Сложность',
        choices=DIFFICULTY_CHOICES,
        blank=True,
        null=True,
    )
    is_active = models.BooleanField(
        default=True,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Выражение'
        verbose_name_plural = 'Выражения'
        ordering = ['word']

    def __str__(self):
        return self.word

    def save(self, *args, **kwargs):
        self.num_r = self.word.lower().count('р')
        super().save(*args, **kwargs)


class ExpressionType(models.Model):
    """Тип выражения/фразы: предложение, скороговорка, текст и т. д."""

    e_type = models.CharField(max_length=50)


class Expression(models.Model):
    """Фраза/выражение, сочетание нескольких слов любой длины."""

    expression = models.TextField('Выражение')
    e_type = models.ManyToManyField(
        ExpressionType,
        verbose_name='Тип выражения',
    )
    length = models.CharField(max_length=50)
    words = models.ManyToManyField(
        Word,
        related_name='e_words',
        verbose_name='Слова в выражении',
    )

    def __str__(self):
        if len(self.expression) < 20:
            return self.expression
        return f'{self.expression[:20]}...'

    class Meta:
        verbose_name = 'Выражение'
        verbose_name_plural = 'Выражения'
        ordering = ['expression']


class UserWord(models.Model):
    """"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )
    word = models.ForeignKey(
        Word,
        on_delete=models.CASCADE,
        verbose_name='Слово',
    )
    is_selected = models.BooleanField(
        'Избранное',
        blank=True,
        null=True,
        help_text='Возможность добавить слово в избранное',
    )
    is_disliked = models.BooleanField(
        'Не нравится',
        blank=True,
        null=True,
        help_text='Возможность исключить слово',
    )

    def __str__(self):
        return


class UserExpression(models.Model):
    """"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )
    expression = models.ForeignKey(
        Expression,
        on_delete=models.CASCADE,
        verbose_name='Выражение',
    )
    is_selected = models.BooleanField(
        'Избранное',
        blank=True,
        null=True,
        help_text='Возможность добавить выражение в избранное',
    )
    is_disliked = models.BooleanField(
        'Не нравится',
        blank=True,
        null=True,
        help_text='Возможность исключить выражение',
    )

    def __str__(self):
        return
