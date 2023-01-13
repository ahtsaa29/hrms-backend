from django.contrib import admin
from django.urls import path, include
from api.views import CompanyViewSet, EmployeeViewSet, PayrollViewSet, LoginViewSet, LogStatViewSet, IssueViewSet, IssueTypeViewSet, DesignationViewSet, ApplicationViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'company', CompanyViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'payroll', PayrollViewSet)
router.register(r'login', LoginViewSet)
router.register(r'logstat', LogStatViewSet)
router.register(r'issue', IssueViewSet)
router.register(r'issuetype', IssueTypeViewSet)
router.register(r'designation', DesignationViewSet)
router.register(r'application', ApplicationViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
