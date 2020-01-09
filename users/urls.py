from django.urls import path
from . import views
from django.views.generic import TemplateView
urlpatterns = [
    path('', TemplateView.as_view(template_name='login.html'), name='index'),
    path('login/', views.logi, name='login'),
    path('batches/', views.batchlist, name='batch'),
    path('faculty_profile/',views.faculty_details,name='facultydetailes'),
    path('student_list/',views.studentlist,name='students'),
    path('student_profile/',views.student_details,name='studentdetails'),
]