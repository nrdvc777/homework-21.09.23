from django.urls import path
from .views import CreateAPiView, ListAPiView, UpdateStatusApiView, AllCommandsApiView

urlpatterns = [
    path('create/', CreateAPiView.as_view()),
    path('all/', ListAPiView.as_view()),
    path('update/<int:news_id>/', UpdateStatusApiView.as_view()),
    
]