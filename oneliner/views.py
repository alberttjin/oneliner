from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from django.contrib.auth.models import User
from django.http import Http404

from .serializers import UserSerializer, TaskSerializer, ProfileSerializer, EventSerializer
from .models import Task, Profile, Event
from .permissions import GetUserPermission, GetTaskPermission, GetEventPermission


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


"""
******************************* TASKS ************************************
"""

class TaskList(APIView):
    """
    GET list of tasks for a specific user
    """

    def get(self, request, format=None):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        user = request.user
        profile = user.profile
        tasks = profile.tasks.all().filter(date__range=(start_date, end_date))
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

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
    
    def post(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            if task:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


"""
******************************* EVENTS ************************************
"""

class AddEvent(APIView):
    """
    POST to create a new event and assign to profile making request
    """

    def post(self, request, format=None):
        user = request.user
        profile = user.profile
        serializer = EventSerializer(data=request.data, context={'profile': profile})
        if serializer.is_valid():
            event = serializer.save()
            if event:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventDetail(APIView):
    """
    View endpoint to GET a specific event from a profile
    """

    permission_classes = (GetEventPermission,)
   
    def get_object(self, pk):
        try:
            event = Event.objects.get(pk=pk)
            self.check_object_permissions(self.request, event)
            return event
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

class EventList(APIView):
    """
    GET list of tasks for a specific user
    """

    def get(self, request, format=None):
        start_date_time = request.query_params.get('start_date_time')
        end_date_time = request.query_params.get('end_date_time')
        user = request.user
        profile = user.profile
        events = profile.events.all().filter(start__range=(start_date_time, end_date_time))
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)