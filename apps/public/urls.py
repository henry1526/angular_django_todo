"""
This is your project's master URL configuration, it defines the set of "root" URLs for the entire project
"""
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('apps.public',
    # Rest Pattern for Todo Items
    url(r'^api/todo/(?P<user_id>[0-9]+)$', 'views.todo_api', name="create_todo"),
    url(r'^user/id$', 'views.get_current_user_id', name="get_current_user_id"),
    # url(r'^todos$', 'views.todos', name="todo_list_html"),
    url(r'^todos-django$', 'views.todos_django', name="todo_list_django"),
    url(r'^logout$', 'views.logout', name="user_logout"),
    url(r'^login$', 'views.login', name="user_login"),
    # url(r'^create$', 'views.create', name="create"),
    url(r'^bmi$', 'views.bmi', name="bmi"),
    url(r'^workout$', 'views.workout', name="workout"),
    url(r'^time$', 'views.time', name="time"),
    url(r'^calories$', 'views.calories', name="calories"),
    url(r'^thanks$', 'views.thanks', name="thanks"),
    url(r'^create_user$','views.create_user', name='create_user'),
    # url(r'^api/location_list$', 'views.location_api', name="location"),
    url(r'^$', 'views.home', name="home"),
    )