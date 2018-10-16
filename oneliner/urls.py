from rest_framework.urlpatterns import format_suffix_patterns

from django.urls import path

from oneliner import views

urlpatterns = [
    path('profiles', views.ProfileList.as_view()),
    path('profiles/<int:pk>', views.ProfileDetail.as_view()),
    path('tasks/<int:pk>', views.TaskDetail.as_view()),
    path('register', views.UserRegister.as_view()),
    path('login', views.UserLogin.as_view(),)
]

urlpatterns = format_suffix_patterns(urlpatterns)