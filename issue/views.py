from django.shortcuts import get_object_or_404
from rest_framework import status

# use Response
from rest_framework.response import Response
# use JsonResponse
from django.http import JsonResponse

# serializers
from issue.serializers import TaskSerializer
# models
from issue.models import Task







# use function base view
# limit Method
from rest_framework.decorators import api_view
# from rest_framework.parsers import JSONParser

# SỬ DỤNG throttle_classes ĐỂ GIỚI HẠN API CHỈ TRUY CẬP 1 LẦN TRONG 1 NGÀY
# from rest_framework.decorators import throttle_classes
# from rest_framework.throttling import UserRateThrottle
# class OncePerDayUserThrottle(UserRateThrottle):
#     rate = '1/day'

@api_view(['GET', 'POST'])
# @throttle_classes([OncePerDayUserThrottle])
# @parser_classes([JSONParser])
def tasks(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response({
            'data': serializer.data,
            'tpl': data
        })

    elif request.method == 'POST':
        # data = {
        #     'title': request.data('title'),
        #     'content': request.data('content'),
        #     'type': request.data('type')
        # }
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE', 'PUT'])
def details(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # serializer.errors tra ve 
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)











# Use APIView
from rest_framework.views import APIView  #giong voi from django.view import View
# from rest_framework.parsers import JSONParser #De cai dat request phai o dang Json

class TasksAPIView(APIView):
    # parser_classes = [JSONParser]

    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)            
        return Response(serializer.data)

    # Create new task 
    def post(self, request):
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

class DetailsAPIView(APIView):
    # parser_classes = [JSONParser]

    def get(self, request, pk=None):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    # Update task
    def put(self, request, pk=None):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete task
    def delete(self, request, pk=None):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)










# Use ViewSet
# C1:
# DUNG DE 'SET' TEN HAM THAY VI SU DUNG CAC HAM MAC DINH NHU get(), get_queryset(),...
from rest_framework import viewsets
class TasksViewSet(viewsets.ViewSet):
    def getTasks(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    def addTask(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# C2: use router.urls
# from issue.views import myViewSet
# from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register(r'my-tasks', myViewSet, basename='myTasks')
# urlpatterns = router.urls

# Tao 1 function moi
from rest_framework.decorators import action

class myViewSet(viewsets.ViewSet):
    # KHI SU DUNG ViewSet thi url luon co dau '/' o cuoi
    # get list
    def list(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    # create new task
    def create(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # get first task
    def retrieve(self, request, pk=None):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TaskSerializer(task)
        return Response(serializer.data)

    # update 1 task
    def update(self, request, pk=None):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        pass
        # PHAN NAY KHONG BIET

    # delete task
    def destroy(self, request, pk=None):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # TAO THE NAY THI SE PHAI DUNG SAU paramater (Ex: http://127.0.0.1:8000/api/issue/my-tasks-viewset/1/add-path-viewset)
    @action(methods=['get'], detail=True, url_path='add-path-viewset')
    def AddPathWiewSet(self, request, pk=None):
        return Response({
            'name': self.name, #name se la ten ham va chuyen thanh kieu chu title (Viet hoa chu cai dau)
            'action': self.action, #ten ham
            'baseview': self.basename,
            'detail': self.detail,
            'suffix': self.suffix,
            'des': self.description
        })













# generics (ListCreateAPIView, RetrieveUpdateDestroyAPIView), get_queryset, JsonResponse,....
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class TasksView(ListCreateAPIView):
    model = Task
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': 'THANH CONG'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'THAT BAI'
        }, status=status.HTTP_400_BAD_REQUEST)

class UpdateTaskView(RetrieveUpdateDestroyAPIView):
    model = Task
    serializer_class = TaskSerializer

    def get_queryset(self, *args, **kwargs):
        return Task.objects.get(pk = kwargs.get('pk'))

    def put(self, request, *args, **kwargs):
        task = get_object_or_404(Task, id=kwargs.get('pk'))
        serializer = TaskSerializer(task, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': 'CAP NHAT THANH CONG'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'CAP NHAT THAT BAI'
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        task = get_object_or_404(Task, id=kwargs.get('pk'))
        task.delete()

        return JsonResponse({
            'message': 'XOA THANH CONG'
        }, status=status.HTTP_200_OK)


# C2:
# Use Generics View (PHAN NAY CHUA LAM DUOC)
from rest_framework import generics
class TasksGenericsView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    # permission_classes = [IsAdminUser]

    # queryset: tu dong tra ve data khi Generics class ko co function get_queryset()
    queryset = Task.objects.all()

    # Get tasks
    def get_queryset(self):
        tasks = Task.objects.all()
        return tasks




