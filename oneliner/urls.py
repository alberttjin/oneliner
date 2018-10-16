from rest_framework.urlpatterns import format_suffix_patterns

from django.urls import path

from oneliner import views

urlpatterns = [
    path('users', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    path('tasks/<int:pk>', views.TaskDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)