from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter(trailing_slash=False) # trailing_slash=False de bo dau '/' cuoi url

app_name = 'issue'

router.register(r'my-tasks-viewset', views.myViewSet, basename='myTasksViewSet')

urlpatterns = [
    path('tasks', views.TasksView.as_view()), #class view
    path('task/<int:pk>', views.UpdateTaskView.as_view()),

    path('c2/tasks', views.tasks), #function view 
    path('c2/task/<int:pk>', views.details),

    path('c3/tasks', views.TasksAPIView.as_view()), #used APIView
    path('c3/task/<int:pk>', views.DetailsAPIView.as_view()),

    path('c4/tasks', views.TasksGenericsView.as_view()), #used Generics
    
    path('c5/tasks', views.TasksViewSet.as_view({'get': 'getTasks', 'post': 'addTask'})), #used ViewSet
    
    # register router.urls if not use urlpatterns += router.urls
    path('', include(router.urls)),
]