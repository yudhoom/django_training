from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.japfa_training.models import *

from django_datatables_view.base_datatable_view import BaseDatatableView
from django.db.models import Q

@login_required
def list_divisions(request):
    #page yg akan ditampilkan
    template = "division/list-divisions.html"    
    return render(request, template)

class list_divisions_json(BaseDatatableView):
    #kolom yg akan ditampilkan
    columns = ['division_code', 'division_name', 'division_description', 'division_status']
    max_display_length = 500

    def get_initial_queryset(self):
        #query
        return mt_division.objects.all()

    def filter_queryset(self, qs):
        # request filter
        search = self.request.POST.get('search[value]', None)
        if search:
            qs = qs.filter(Q(division_code__icontains=search) | 
                            Q(division_name__icontains=search) |
                            Q(division_description__icontains=search) | 
                            Q(division_status__icontains=search))

        return qs
    
    def prepare_results(self, qs):
        # data yg akan ditampilkan
        json_data = []
        for item in qs:
            json_data.append([
                item.division_code,
                item.division_name,
                item.division_description,
                item.division_status == 'A' if 'Active' else 'Inactive',
            ])
        return json_data
