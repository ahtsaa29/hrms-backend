from rest_framework import serializers
from api.models import Company, Employee, Payroll, Login, LogStat, Issue, IssueType, Designation, Application

#create serializers
class CompanySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Company
        fields= "__all__"

    def validate_phone(self, value):
        if value < 9000000000 or value > 9999999999:
            raise serializers.ValidationError('wrong format')
        return value

class EmployeeSerializer (serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields= "__all__"
        
    def validate_phone(self, value):
        if value < 9000000000 or value > 9999999999:
            raise serializers.ValidationError('wrong format')
        return value
        
class PayrollSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payroll
        fields= "__all__"
    salary = serializers.ReadOnlyField()
    tax_amount = serializers.ReadOnlyField()
    gross_salary = serializers.ReadOnlyField()
    net_salary = serializers.ReadOnlyField()

class LoginSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Login
        fields= "__all__"

class LogStatSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LogStat
        fields= "__all__"
    time_of_login = serializers.ReadOnlyField()
    time_of_logout = serializers.ReadOnlyField()

class EmployeeSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields= "__all__"

class ApplicationSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Application
        fields= "__all__"


class IssueSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Issue
        fields= "__all__"

class IssueTypeSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IssueType
        fields= "__all__"

class DesignationSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Designation
        fields= "__all__"