from django.urls import path
from . import views
app_name = 'polls'
urlpatterns = [
    path('', views.index, name="homePolls"),
    path('details/<int:user_id>', views.show, name='details'),
    path('create', views.create, name='create'),
    path('store', views.store, name='store'),
    # path('upload-file', views.upload_file, name='uploadFile'),

    path('login', views.loginUser, name='login'),
]
