from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as rest_framework_views

from django.urls import path

from oneliner import views

urlpatterns = [
    path('profiles', views.ProfileList.as_view()),
    path('profiles/<int:pk>', views.ProfileDetail.as_view()),
    path('tasks/<int:pk>', views.TaskDetail.as_view()),
    path('tasks', views.TaskList.as_view()),
    path('add-task', views.AddTask.as_view()),
    path('complete-task', views.CompleteTask.as_view()),
    path('register', views.UserRegister.as_view()),
    path('login', rest_framework_views.obtain_auth_token),
    path('events', views.EventList.as_view()),
    path('events/<int:pk>', views.EventDetail.as_view()),
    path('add-event', views.AddEvent.as_view()),
    path('complete-event', views.CompleteEvent.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)