from django.test import TestCase

# Create your tests here.

from test_dj.models import Poll,Choice

import datetime

from django.utils import timezone

class PollTest(TestCase):
    def test_was_pub_recently(self):
        
        future_poll=Poll(pub_date=timezone.now()+datetime.timedelta(days=30))
        self.assertEqual( future_poll.was_pub_recently(),True);
    
    def test_question(self):
        
        none_question=Poll(question='this is not none')
        self.assertEqual(none_question.question, None, 'equal')
        