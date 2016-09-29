from django.conf.urls import include, url
from django.contrib import admin

# location mysite/mysite/

# Examples:
# url(r'^$', 'mysite.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),
urlpatterns = [ url(r'^polls/', include('polls.urls', namespace='polls')),
                url(r'^admin/', admin.site.urls)]
