from django.shortcuts import render
from users.models import login, faculties, Students
from django.contrib.auth import authenticate
from django.http import HttpResponse

# Create your views here.
#user login
fac_id=0
def logi(request):

    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')

        p = login.objects.get(password=password)
        u = login.objects.get(username=username)
        type = u.type


        if type == 'faculty' and u.password==password:
            batch = faculties.objects.get(email=username)
            context = {'batchs': batch}
            return render(request,'admin_batch.html',context)
        elif type == 'student' and u.password==password:
            id=Students.objects.get(email=username)
            return render(request,'studentpage.html',{'student':id})
        else:
            return HttpResponse("Error Login")
    else:
        return HttpResponse("Something Went Wrong")

print(fac_id)


def student(request):
    return render(request,'student_list.html')

#admin faculty details table views
def faculty_details(request):

    ab =  request.GET.get('a')
    print(ab)
    facultyview = faculties.objects.get(id=ab)
    print(facultyview)
    return render (request, 'admin_faculties_details.html', {'batchs': facultyview} )

#Batch view of faculty
def batchlist(request):

    ab =  request.GET.get('id')
    print(ab)
    batch = faculties.objects.get(id=ab)

    return render(request,'admin_batch.html',{'batchs':batch})

def student_details(request):

    ab = request.GET.get('id')
    studentss = Students.objects.get(id=ab)
    print(studentss.name)
    return render (request, 'studentprofile.html', {'student': studentss} )

def studentlist(request):


#login
# def login_request(request):
#
#      if request.method=='POST':
#         email= request.POST.get('email')
#         password = request.POST.get('password')
#         email=str(email)
#         password=str(password)
#         u=signup.objects.filter(password=password)ba
#         p=signup.objects.filter(email=email)
#         c=0
#         if u.count()==1 and p.count()==1:
#             print("hai")
#             c+=1
#             QuerySet = signup.objects.all().filter( email = email )
#             if c==1:
#                 return render(request,'admin_home.html',{'data':QuerySet})
#             else:
#                 return HttpResponse("you are not logged in")
#         return HttpResponse("you are not logged in")
#
#

# #admin faculty details table views
# def admin_faculty_detail(request):
#     ab = request.GET.get('id')
#     print(ab)
#     facultyview = faculties.objects.get(id=ab)
#     print(facultyview)
#     return render(request, 'admin_faculties_details.html', {'faculty': facultyview})
#
#
# #faculty registration by admin
# def facultyadd(request):
#     if request.method == 'POST':
#         fname = request.POST.get('fname')
#         faddress = request.POST.get('faddress')
#         fmobile = request.POST.get('fmobile')
#         femail = request.POST.get('femail')
#         fqualification = request.POST.get('fqualification')
#         fpassword = request.POST.get('fpassword')
#         fbatch = request.POST.get('fbatch')
#
#         a = faculties(f_name=fname, f_address=faddress, f_mobile=fmobile, f_email=femail, f_qualfication=fqualification, f_password=fpassword, f_batch=fbatch)
#         a.save()
#     return render(request,'admin_faculties.html')
#
# #display corresponding faculty details
# def admin_faculty_details(request):
#     facultydetails = faculties.objects.all.filter()
#     print(facultydetails)
#     return render (request,'admin_faculties.html',{'faculty':facultyview})
#
#  #get batch details
#
# def admin_batch_table(request):
#     batchview = batches.objects.all()
#     print(facultyview)
#     return render (request,'admin_batch.html',{'batches':batchview})