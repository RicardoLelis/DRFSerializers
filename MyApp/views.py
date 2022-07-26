from django.shortcuts import render


from rest_framework import viewsets
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

class StudentModel(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
