from django.test import TestCase

import datetime
from django.utils import timezone
from django.urls import reverse

from .models import Type, Algorithm

# Test Model
class TypeModelTests(TestCase):

    #1.1 returns False for types whose create_date is in the future.
    def test_was_created_recently_with_future_type(self):
        time = timezone.now() + datetime.timedelta(days=30)
        mytype = Type(create_date=time)
        self.assertIs(mytype.was_created_recently(), False)

    #1.2 returns False for types whose create_date  is older than 1 day.
    def test_was_created_recently_with_old_type(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        mytype = Type(create_date=time)
        self.assertIs(mytype.was_created_recently(), False)

    #1.3 returns True for types whose create_date is within the last day.
    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        mytype = Type(create_date=time)
        self.assertIs(mytype.was_created_recently(), True)


    #2. Create a type with the given `type_text` and 
    #  created the given number of `days` offset to now (negative for created in the past, positive that have yet to be created).
    
def create_type(type_text, days):
    
    time = timezone.now() + datetime.timedelta(days=days)
    return Type.objects.create(type_text=type_text, create_date=time)


class TypeIndexViewTests(TestCase):
    # If no types exist, an appropriate message is displayed.
    def test_no_types(self):
        response = self.client.get(reverse('algorithms:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No algorithms are available.")
        self.assertQuerysetEqual(response.context['latest_algorithm_list'], [])

    # Types with a create_date in the past are displayed on the index page.   
    def test_past_type(self):
        create_type(type_text="Past type.", days=-30)
        response = self.client.get(reverse('algorithms:index'))
    
        self.assertQuerysetEqual(
            response.context['latest_algorithm_list'],
            ['<Type: Past type.>']
        )

    # def test_future_question(self):
    #     """
    #     Questions with a pub_date in the future aren't displayed on
    #     the index page.
    #     """
    #     create_question(question_text="Future question.", days=30)
    #     response = self.client.get(reverse('polls:index'))
    #     self.assertContains(response, "No polls are available.")
    #     self.assertQuerysetEqual(response.context['latest_question_list'], [])

    # def test_future_question_and_past_question(self):
    #     """
    #     Even if both past and future questions exist, only past questions
    #     are displayed.
    #     """
    #     create_question(question_text="Past question.", days=-30)
    #     create_question(question_text="Future question.", days=30)
    #     response = self.client.get(reverse('polls:index'))
    #     self.assertQuerysetEqual(
    #         response.context['latest_question_list'],
    #         ['<Question: Past question.>']
    #     )

    # def test_two_past_questions(self):
    #     """
    #     The questions index page may display multiple questions.
    #     """
    #     create_question(question_text="Past question 1.", days=-30)
    #     create_question(question_text="Past question 2.", days=-5)
    #     response = self.client.get(reverse('polls:index'))
    #     self.assertQuerysetEqual(
    #         response.context['latest_question_list'],
    #         ['<Question: Past question 2.>', '<Question: Past question 1.>']
    #     )