from django.urls import path
from .views import TaskApiVuew, TaskDetail

urlpatterns = [
    path('', TaskApiVuew.as_view()),
    path('<int:pk>', TaskDetail.as_view()),
]