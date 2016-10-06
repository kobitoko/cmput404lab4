import datetime
from django.utils import timezone
from polls.models import Question
# create a question that was published 60 days ago
past_question = Question(pub_date=timezone.now() - datetime.timedelta(days=60))
print("was 60 day old published recently?:")
print(past_question.was_published_recently())
# create a question instance with pub_date 30 days in the future
future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=30))
# was it published recently?
print("was future post published recently?:")
print(future_question.was_published_recently())


