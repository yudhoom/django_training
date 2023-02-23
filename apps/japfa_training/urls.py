# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from django.conf.urls import url
from apps.japfa_training.views import views
from apps.japfa_training.views import division, employee

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # Division
    path('master/list-divisions', division.list_divisions, name='list_divisions'),
    re_path(r'^master/list-divisions/data/$', division.list_divisions_json.as_view(), name='list_divisions_json'),

    # Employee
    path('master/list-employees', employee.list_employees, name='list_employee'),
    re_path(r'^master/list-employees/data/$', employee.list_employees_json.as_view(), name='list_employees_json'),
    path('master/create-employee', employee.create_employee.as_view(), name='create_employee'), #create emploeyee
    path('master/update-employee', employee.update_employee.as_view(), name='update_employee'), #edit emploeyee
    path('master/delete-employee', employee.delete_employee, name='delete_employee'), #delete emploeyee

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
]
