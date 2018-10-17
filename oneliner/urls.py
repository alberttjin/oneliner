from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as rest_framework_views

from django.urls import path

from oneliner import views

urlpatterns = [
    path('profiles', views.ProfileList.as_view()),
    path('profiles/<int:pk>', views.ProfileDetail.as_view()),
    path('tasks/<int:pk>', views.TaskDetail.as_view()),
    path('register', views.UserRegister.as_view()),
    path('login', rest_framework_views.obtain_auth_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)