from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from django.contrib.auth.models import User
from django.http import Http404

from .serializers import UserSerializer, TaskSerializer, ProfileSerializer
from .models import Task, Profile
from .permissions import GetUserPermission, GetTaskPermission


# Create your views here.
class ProfileList(APIView):
    """
    View endpoint to GET list of all profiles. Should never be used from client side, only for debugging, set
    authentication class to admin only
    """
    authentication_classes = ()
    permission_classes = ()

    def get(self, request, format=None):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)
    
class UserRegister(APIView):
    """
    View endpoint to register user by POST request of username, email, and password. Requires no authentication
    """
    authentication_classes = ()
    permission_classes = ()

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UserLogin(APIView):
#     """
#     View endpoint to login user by POST request of username or email and password
#     """
#     def post(self, request, *args, **kwargs):
#         serializer = UserLoginSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileDetail(APIView):
    """
    View endpoint to GET the profile of a specific user through id sent in url stored in variable pk.  
    """
    permission_classes = (GetUserPermission,)

    def get_object(self, pk):
        try:
            user = User.objects.get(pk=pk)
            self.check_object_permissions(self.request, user)
            return user
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        profile = user.profile
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

class TaskList(APIView):
    """
    GET list of tasks for a specific user
    """

    def get(self, request, format=None):
        user = request.user
        profile = user.profile
        tasks = profile.tasks.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

class AddTask(APIView):
    """
    POST to create a new task and assign it to the user making the request
    """
    
    def post(self, request, format=None):
        user = request.user
        profile = user.profile
        serializer = TaskSerializer(data=request.data, context={'profile': profile})
        if serializer.is_valid():
            task = serializer.save()
            if task:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetail(APIView):
    """
    View endpoint to GET a specific task for a specific user.
    """
    permission_classes = (GetTaskPermission,)
   
    def get_object(self, pk):
        try:
            task = Task.objects.get(pk=pk)
            self.check_object_permissions(self.request, task)
            return task
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)
