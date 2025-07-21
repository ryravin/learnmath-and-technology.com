from django.shortcuts import render, redirect
from .models import Student, Book
from rest_framework import generics
from .serializers import StudentSerializer, BookSerializer
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    return render(request, 'myapp/index.html')

def math(request):
    books = Book.objects.filter(category='math')
    return render(request, 'myapp/math.html', {'books': books})

def technology(request):
    books = Book.objects.filter(category='technology')
    return render(request, 'myapp/technology.html', {'books': books})

def bacci(request):
    books = Book.objects.filter ( category='bacci' )
    return render(request,'myapp/bacci.html', {'books': books})

def lean_ai(request):
    books=Book.objects.filter(category='learn_ai')
    return render(request,'myapp/leanai.html', {'books': books})

def test(request):
    return render(request,'myapp/test.html')

def login(request):
     if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('index')  # redirect to homepage after login
        else : 
            messages.error(request, 'Invalid email or password.')
            return redirect('index')
     else:
        form = AuthenticationForm()
     return render(request,'myapp/loing.html', {'form': form})

class StudentListCreate(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
