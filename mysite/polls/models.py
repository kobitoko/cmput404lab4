from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
# This is going to be a table
class Question(models.Model):
    # This going to be a column field in the Question table.
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date publised')
    # Override standard string method and prints something useful for the client.
    def __str__(self):
        return self.question_text
    
@python_2_unicode_compatible
# This is going to be a table
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    # Create integer field in DB, for ppl to vote.
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

