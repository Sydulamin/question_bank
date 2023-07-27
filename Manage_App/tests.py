
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import User, Question

class UserQuestionStatsTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create(idname='user1', display_name='User One', email='user1@example.com', phone='1234567890')
        self.user2 = User.objects.create(idname='user2', display_name='User Two', email='user2@example.com', phone='9876543210')

        self.question1 = Question.objects.create(
            question='Question 1',
            option1='Option A',
            option2='Option B',
            option3='Option C',
            option4='Option D',
            option5='Option E',
            answer=1,
            explain='Explanation 1',
        )
        self.question2 = Question.objects.create(
            question='Question 2',
            option1='Option A',
            option2='Option B',
            option3='Option C',
            option4='Option D',
            option5='Option E',
            answer=2,
            explain='Explanation 2',
        )

        self.user1.favorited_questions.add(self.question1)
        self.user1.read_questions.add(self.question2)
        self.user2.favorited_questions.add(self.question2)
        self.user2.read_questions.add(self.question1)

    def test_user_question_stats(self):
        url = reverse('user-question-stats')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2) 
        self.assertEqual(response.data[0]['favorite_count'], 1)
        self.assertEqual(response.data[0]['read_count'], 1)
        self.assertEqual(response.data[1]['favorite_count'], 1)
        self.assertEqual(response.data[1]['read_count'], 1)

    def test_filter_questions(self):
        self.client.force_login(self.user1)

        url = reverse('filter-questions')
        response = self.client.get(url, {'status': 'read'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1) 

        response = self.client.get(url, {'status': 'unread'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1) 

        response = self.client.get(url, {'status': 'favorite'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1) 
        response = self.client.get(url, {'status': 'unfavorite'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1) 

    def test_filter_questions_no_status(self):
        url = reverse('filter-questions')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  
        response = self.client.get(url, {'status': 'invalid'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2) 

        response = self.client.get(url, {'status': ''})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2) 
