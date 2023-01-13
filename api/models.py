from django.db import models
from datetime import datetime

# Create your models here.

# Designation Model
class Designation(models.Model):
    designation_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    salary = models.DecimalField(max_digits=8, decimal_places=2,default=0)

    def __str__(self):
        return self.name


# IssueType Model
class IssueType(models.Model):
    issue_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


# Company Model for settings
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='uploads/logo', height_field=None, width_field=None, max_length=100)
    pan_no = models.BigIntegerField()
    added_date = models.DateTimeField(default=datetime.now, editable=False)
    # save logo in custom name and location


# Employee Model
class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=100)
    pan_no = models.BigIntegerField()
    image = models.ImageField(upload_to='uploads/employee/employee_id', height_field=None, width_field=None, max_length=100)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE, default=None)
    joined_date = models.DateTimeField(default=datetime.now, editable=False)

    def __str__(self):
        return self.first_name 


# Payroll Model
class Payroll(models.Model):
    payroll_id = models.AutoField(primary_key=True)
    designation =models.ForeignKey(Designation, on_delete=models.CASCADE, default=None)
    salary = models.DecimalField(max_digits=6, decimal_places=2,default=None)
    gross_salary = models.DecimalField(max_digits=8, decimal_places=2)
    tax_percent = models.DecimalField(max_digits=8, decimal_places=2)
    tax_amount = models.DecimalField(max_digits=8, decimal_places=2)
    overtime = models.DecimalField(max_digits=8, decimal_places=2)
    allowance = models.DecimalField(max_digits=8, decimal_places=2)
    bonus = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    medical_claim = models.DecimalField(max_digits=8, decimal_places=2)
    net_salary = models.FloatField()
    employee = models.OneToOneField(Employee,on_delete=models.CASCADE, default=None)
    updated_at = models.DateTimeField(default=datetime.now, editable=False)

    def save(self, *args, **kwargs):
        self.salary = self.designation.salary
        self.gross_salary = self.designation.salary + self.overtime + self.allowance + self.bonus + self.medical_claim
        self.tax_amount = (self.gross_salary * self.tax_percent)/100
        self.net_salary = self.gross_salary - self.tax_amount

    def __str__(self):
        return self.designation.name + "-" + self.salary
    

# Login Model
class Login(models.Model):

    # face recognition
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    image = models.CharField(max_length=25, default="photo of person")


# LogStat Model
class LogStat(models.Model):
    is_login = models.BooleanField(default=None)
    if is_login == True:
        time_of_login = models.DateTimeField(default=datetime.now, editable=False)
        time_of_logout = models.CharField(max_length=25 , default="Still Logged In")
    else: 
        time_of_login = models.CharField(max_length=25 ,default="haven't Logged In")
        time_of_logout = models.DateTimeField(default=datetime.now, editable=False)
    leave_days = models.IntegerField()
    leave_count = models.IntegerField()
    is_late = models.BooleanField()
    is_attendance_low = models.BooleanField()
    is_late_for_thrice = models.BooleanField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, default=None)

    # time stamp corresponding to face recog
    # login logout


# Issue Model
class Application(models.Model):
    application_id = models.AutoField(primary_key=True)
    apply_for = models.ForeignKey(IssueType, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=25)
    reason = models.TextField()
    date = models.DateTimeField(default=datetime.now, editable=False)
    for_days = models.IntegerField()


class Issue(models.Model):
    issue_id = models.AutoField(primary_key=True)
    STATUS = (
        ('Approved','Approved'),
        ('Declined','Declined'),
        ('Pending','Pending')
    )
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, default=None)
    issue = models.ManyToManyField(Application, default=None)
    status = models.CharField(max_length=25, choices=STATUS, default=0)
    def __str__(self):
        return self.issue.name