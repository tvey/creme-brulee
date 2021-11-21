from django.contrib import admin

from .models import Word, Expression, ExpressionType, UserWord, UserExpression

admin.site.register(Word)
admin.site.register(ExpressionType)
admin.site.register(Expression)
admin.site.register(UserWord)
admin.site.register(UserExpression)
