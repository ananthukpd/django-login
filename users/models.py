from django.db import models


# Create your models here.

# faculty table

class faculties(models.Model):
    emp_id = models.IntegerField()
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=20, null=True, blank=True)
    j_date = models.DateField(max_length=20)
    qualification = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)
    mobile = models.IntegerField()
    email = models.CharField(max_length=50)
    batch = models.CharField(max_length=10, null=True, blank=True)
    blood = models.CharField(max_length=20, null=True, blank=True)
    dob = models.DateField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'faculty_details'


class Students(models.Model):
    ad_no = models.IntegerField()
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    qualification = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50)
    gender = models.CharField(max_length=20, null=True, blank=True)
    course = models.CharField(max_length=50)
    batch = models.CharField(max_length=50)
    dob = models.DateField(null=True, blank=True)
    ad_date = models.DateField()
    f_name = models.CharField(max_length=50, null=True, blank=True)
    m_name = models.CharField(max_length=50, null=True, blank=True)
    blood = models.CharField(max_length=20, null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    p_mobile = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    religion = models.CharField(max_length=20, null=True, blank=True)
    category = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        db_table = 'student_details'


# Login table

class login(models.Model):
    user_id = models.IntegerField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    l_login = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'login'

# Leave table

class Leave(models.Model):
    user_id = models.IntegerField()
    leave_id = models.IntegerField()
    status = models.CharField(max_length=50)
    reason = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    date_from = models.DateField()
    date_to = models.DateField()
    date_app = models.DateField()
    session = models.CharField(max_length=20)
    fac_id = models.CharField(max_length=20)

    class Meta:
        db_table = 'leave'


# Assessment Table
class Assessment(models.Model):
    Ass_id = models.CharField(max_length=50)
    fac_id = models.CharField(max_length=50)
    detail = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    batch = models.CharField(max_length=50)
    total = models.IntegerField()
    date_ass = models.DateField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'assessment'

#class Table

class Class(models.Model):
    course = models.CharField(max_length=50)
    batch = models.CharField(max_length=50)
    fac_id = models.IntegerField()
    room = models.CharField(max_length=50)

    class Meta:
        db_table = 'Class'

#Attendance Table
class Attendance(models.Model):
    s_id = models.IntegerField()
    fac_id = models.IntegerField()
    status = models.CharField(max_length=50)
    date = models.DateField()
    hour = models.BinaryField()

    class Meta:
        db_table = 'Attendance'

#Result Table
class Result(models.Model):
    s_id = models.CharField(max_length=50)
    fac_id = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    date = models.DateField()
    hour = models.BinaryField()

    class Meta:
        db_table = 'Result'











