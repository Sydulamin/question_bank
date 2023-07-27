import os
import django
import random
import string
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Question_Management.settings')
django.setup()

from Manage_App.models import User, Question

faker = Faker()

def generate_users(num_users):
    users = []
    for _ in range(num_users):
        users.append(User(
            idname=faker.unique.user_name(),
            display_name=faker.name(),
            email=faker.email(),
            phone=faker.phone_number(),
        ))
    return users

def generate_questions(num_questions):
    questions = []
    for _ in range(num_questions):
        questions.append(Question(
            question=faker.sentence(nb_words=10),
            option1=faker.sentence(nb_words=5),
            option2=faker.sentence(nb_words=5),
            option3=faker.sentence(nb_words=5),
            option4=faker.sentence(nb_words=5),
            option5=faker.sentence(nb_words=5),
            answer=random.randint(1, 5),
            explain=faker.paragraph(nb_sentences=2),
        ))
    return questions

def save_data(objects):
    with transaction.atomic():
        for obj in objects:
            obj.save()

if __name__ == "__main__":
    num_users = 10000000
    num_questions = 1000000

    users = generate_users(num_users)
    questions = generate_questions(num_questions)

    print("Saving Users...")
    save_data(users)
    print("Users saved successfully!")

    print("Saving Questions...")
    save_data(questions)
    print("Questions saved successfully!")
