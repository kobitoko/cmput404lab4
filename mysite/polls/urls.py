from django.conf.urls import url
from . import views

# mysite/polls/

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    # Note the r'^(?P<question_id>[0-9]+)/$' and r'^(?P<question_id>[0-9]+)$' <- (missing the end "/"). 
    # are different, if u do without the "/" it 404s
    # Also add [A-Z] or [a-z] to allow alphabetical characters.
    #pk is short for PrimaryKey
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote')
]

