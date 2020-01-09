from django.contrib import admin
from users.models import faculties, login,Students

# Register your models here.
admin.site.register(faculties)
admin.site.register(login)
admin.site.register(Students)
# class faculties(admin.ModelAdmin):
#     list_display = ['emp_id', 'name', 'j_date','mobile', 'email', 'batch']

