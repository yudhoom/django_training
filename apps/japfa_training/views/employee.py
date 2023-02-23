from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import UpdateView
from django.db import transaction
from django.http import JsonResponse
from apps.japfa_training.models import *
from datetime import datetime
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.db.models import Q

@login_required
def list_employees(request):
    #page yg akan ditampilkan
    template = "employee/list-employees.html"    
    return render(request, template)

class list_employees_json(BaseDatatableView):
    #kolom yg akan ditampilkan
    columns = ['empid', 'empname', 'email', 'gender', 'url_photo']
    max_display_length = 500

    def get_initial_queryset(self):
        #query
        return mt_employee.objects.all()

    def filter_queryset(self, qs):
        # request filter
        search = self.request.POST.get('search[value]', None)
        if search:
            qs = qs.filter(Q(empid__icontains=search) | 
                           Q(empname__icontains=search) | 
                           Q(email__icontains=search) | 
                           Q(gender__icontains=search) | 
                           Q(url_photo__icontains=search))

        return qs
    
    def prepare_results(self, qs):
        # data yg akan ditampilkan
        json_data = []
        for item in qs:
            json_data.append([
                item.empid,
                item.empname,
                item.email,
                "Male" if item.gender == "M" else "Female", #ternary operator
                item.url_photo,
                "<a class='btn btn-primary btn-sm update-modal' data-url='/master/update-employee?id_employee="+ str(item.id_employee) + "'><i class='fas fa-edit'></i></a> <a class='btn btn-danger btn-sm' href='#' data-id="+ str(item.id_employee) +" data-empname='"+ item.empname +"' onClick='deleteFunction(this)'><i class='fas fa-trash'></i></a>",
            ])
        
        #return data yg akan ditampilkan
        return json_data
    
class create_employee(UpdateView): 
    def get(self, request):
        template = "employee/create-employee.html"

        division = mt_division.objects.all().order_by('division_name') 
        
        context = {
            'division': division,
        }
        return render(request, template, context)
    
    def post(self, request):
        data = request.POST

        try:
            with transaction.atomic():

                mt_employee.objects.create(
                    mt_division_id = data['division'],
                    empid = data['empid'],
                    empname = data['empname'],
                    email = data['email'],
                    gender = data['gender'],
                    url_photo = data['photo'],
                    created_by = 'admin',
                    created_at = datetime.now()
                )
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': 'Failed save data.'})

        return JsonResponse({'status': 'success', 'message': 'Success save data.'})
    
class update_employee(UpdateView):
    def get(self, request):
        id_employee = self.request.GET.get('id_employee')

        employee  = mt_employee.objects.filter(id_employee=id_employee).first()
        
        division = mt_division.objects.all().order_by('division_name')

        context = {
            'employee': employee,
            'division': division
        }
        return render(request, 'employee/update-employee.html', context)
    
    def post(self, request):
        if request.method == 'POST':
            data = request.POST
            try:
                with transaction.atomic():
                   if data['id_employee'] is not None:

                        employee = mt_employee.objects.get(id_employee=data['id_employee'])
                        employee.mt_division_id = data['division']
                        employee.empid = data['empid']
                        employee.empname = data['empname']
                        employee.email = data['email']
                        employee.url_photo = data['photo']
                        employee.gender = data['gender']
                        employee.save()

                        return JsonResponse({'status': 'success', 'message': 'Success update employee.'})
            except:
                return JsonResponse({'status': 'error', 'message': 'Failed update employee.'})

def delete_employee(request):
    if request.method == 'POST':
        data = request.POST
        print(request.POST)
        try:
            with transaction.atomic():
                mt_employee.objects.filter(id_employee=data['id']).delete()
                return JsonResponse({'status': 'success', 'message': 'Success delete employee.'})
        except:
            return JsonResponse({'status': 'error', 'message': 'Failed delete employee.'})
