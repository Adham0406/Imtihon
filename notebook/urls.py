
from django.urls import path
from .views import NotebookListView, NotebookDetailApiView, NotebookCreateApiView,  NotebookdeleteView, NotebookUpdateApiView, NotebookMixedApiView

urlpatterns = [
    path('notebooklar/', NotebookListView.as_view()),
    path('notebook/<int:pk>/', NotebookDetailApiView.as_view()),
    path('notebook/create/',  NotebookCreateApiView.as_view()),
    path('notebook/delete/<int:pk>/', NotebookdeleteView.as_view()),
    path('notebook/update/<int:pk>/', NotebookUpdateApiView.as_view()),
    path('notebook/mixed/<int:pk>/', NotebookMixedApiView.as_view())
]