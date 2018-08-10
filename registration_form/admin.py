from django.contrib import admin
from .models import Register
from django.shortcuts import render
from django.http import Http404
from django.conf.urls import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources


# class RegistrationExporterResource(resources.ModelResource):
#     class Meta:
#         model = Register
#         exclude = ('id',)
#         import_id_fields = ('phno','fullname', 'gender' , 'emailid','location' , 'teesize' , 'prevruns', 'dob')
#         skip_unchanged = True
#         fields =  ('phno','fullname', 'gender' , 'emailid','location' , 'teesize' , 'prevruns', 'dob')
#         export_order = ('phno','fullname', 'gender' , 'emailid','location' , 'teesize' , 'prevruns', 'dob')


class RegistrationResource(ImportExportModelAdmin):
    pass

# class RegisterAdmin(admin.ModelAdmin):
#     #resource_class = RegistrationResource
#     change_list_template = 'details_chart.html'


admin.site.register(Register,RegistrationResource)
