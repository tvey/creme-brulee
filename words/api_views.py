from itertools import chain

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Word, Expression
from .serializers import WordExpSerializer


@api_view(['GET'])
def search(request):
    items = {}
    search_query = request.query_params.get('q')
    print(search_query)

    if search_query:
        words = Word.objects.filter(content__icontains=search_query)
        expressions = Expression.objects.filter(content__icontains=search_query)
        items = chain(words, expressions)
    serializer = WordExpSerializer(items, many=True)
    print(serializer.data)
    return Response(serializer.data)
