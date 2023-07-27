from django.urls import path
from . import views

urlpatterns = [
    path('user-question-counts/', views.user_question_counts, name='user-question-counts'),
    path('filter-questions/', views.filter_questions, name='filter-questions'),
]
