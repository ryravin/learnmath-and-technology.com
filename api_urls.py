# myapp/urls_api.py
from django.urls import path
from .views import StudentListCreate, StudentDetail, BookListCreate, BookDetail

urlpatterns = [
    path('students/', StudentListCreate.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentDetail.as_view(), name='student-detail'),
    path('books/', BookListCreate.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
]
