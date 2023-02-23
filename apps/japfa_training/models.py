# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class mt_division(models.Model):
    id_division = models.AutoField(primary_key=True)
    division_code = models.CharField(max_length=10)
    division_name = models.CharField(max_length=50)
    division_description = models.CharField(max_length=100)
    division_status = models.CharField(max_length=1)
    created_by = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=20, null=True)
    updated_at = models.DateTimeField(auto_now=False,null=True)
    class Meta:
        verbose_name_plural = "mt_division"
        db_table = 'mt_division'
class mt_employee(models.Model):
    id_employee = models.AutoField(primary_key=True)
    mt_division = models.ForeignKey(mt_division, db_column='id_division', related_name="mt_employee_mt_division", on_delete=models.CASCADE)
    empid = models.CharField(max_length=20)
    empname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    gender = models.CharField(max_length=1)
    url_photo = models.CharField(max_length=100)
    created_by = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=20, null=True)
    updated_at = models.DateTimeField(auto_now=False,null=True)

    class Meta:
        verbose_name_plural = "mt_employee"
        db_table = 'mt_employee'
class mt_user(models.Model):
    id_user = models.AutoField(primary_key=True)
    mt_employee = models.ForeignKey(mt_employee, db_column='id_employee', related_name="mt_user_mt_employee", on_delete=models.CASCADE)
    password = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "mt_user"
        db_table = 'mt_user'
