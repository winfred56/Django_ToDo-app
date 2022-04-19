from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/<int:pk>/', views.TaskDetail.as_view(), name='detail'),
    path('tasks/<int:pk>/delete/', views.TaskDelete.as_view(), name='delete'),
    path('tasks/new/', views.AddNew.as_view(), name='new'),

]