from django.shortcuts import render
from rest_framework import viewsets, serializers
from api.models import Company, Employee, Payroll, Login, LogStat, Issue, IssueType, Designation, Application

from api.serializers import CompanySerializer, EmployeeSerializer, PayrollSerializer, LoginSerializer, LogStatSerializer, IssueSerializer, IssueTypeSerializer, DesignationSerializer, ApplicationSerializer
# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    company_id = serializers.ReadOnlyField()
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class PayrollViewSet(viewsets.ModelViewSet):
    queryset = Payroll.objects.all()
    serializer_class = PayrollSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class LoginViewSet(viewsets.ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer

class LogStatViewSet(viewsets.ModelViewSet):
    queryset = LogStat.objects.all()
    serializer_class = LogStatSerializer

class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

class IssueTypeViewSet(viewsets.ModelViewSet):
    queryset = IssueType.objects.all()
    serializer_class = IssueTypeSerializer

class DesignationViewSet(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
