from rest_framework import serializers

from .models import Word, Expression, ExpressionType


class WordExpSerializer(serializers.Serializer):
    content = serializers.CharField()


class ExpressionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpressionType
        fields = ['id', 'e_type']


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = [
            'id',
            'content',
            'num_r',
            'in_stressed',
            'part_of_speech',
        ]


class ExpressionSerializer(serializers.ModelSerializer):
    e_types = ExpressionTypeSerializer(read_only=True, many=True)

    class Meta:
        model = Expression
        fields = [
            'id',
            'content',
            'e_types',
        ]
