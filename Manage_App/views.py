from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.views import APIView
from .models import User, Question, FavoriteQuestion, ReadQuestion
from .serializers import UserSerializer, QuestionSerializer

class CustomUserPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

@api_view(['GET'])
@cache_page(60)  
def user_question_counts(request):
    user_stats = []
    users = User.objects.all().prefetch_related('favoritequestion', 'readquestion')
    for user in users:
        favorite_count = user.favoritequestion.count()
        read_count = user.readquestion.count()
        user_stats.append({
            'user_id': user.id,
            'display_name': user.display_name,
            'favorite_count': favorite_count,
            'read_count': read_count,
        })
    return Response(user_stats)

@api_view(['GET'])
@cache_page(60)  
def filter_questions(request):
    status = request.query_params.get('status', None)
    user = request.user  
    if status == 'read':
        questions = Question.objects.filter(readquestion__user=user)
    elif status == 'unread':
        questions = Question.objects.exclude(readquestion__user=user)
    elif status == 'favorite':
        questions = Question.objects.filter(favoritequestion__user=user)
    elif status == 'unfavorite':
        questions = Question.objects.exclude(favoritequestion__user=user)
    else:
        return Response({'detail': 'Invalid status parameter.'}, status=status.HTTP_400_BAD_REQUEST)

    paginator = CustomUserPagination()
    page = paginator.paginate_queryset(questions, request)
    serializer = QuestionSerializer(page, many=True)
    return paginator.get_paginated_response(serializer.data)
