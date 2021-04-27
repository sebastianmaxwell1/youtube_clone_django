from django.urls import path
from .myproject import views

urlpatterns = [
    path('videos/', views.VideoList.as_view()),
]