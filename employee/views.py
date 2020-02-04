from django.shortcuts import render
# Create your views here.
from .models import Employee
from .serializers import EmployeeSerializer #self made serializer
from.serializers import UserSerializer #for the user
from rest_framework import generics

#Shows the EmployeeList
class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]

    #method to relate
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    #adding permission

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = EmployeeSerializer

    