from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q 
from .models import Fault, AffectedResident 


def explorer_map(request):
    query = request.GET.get('search', '').strip()
    faults = Fault.objects.all().order_by('-date_reported')

    if query:
       
        search_map = {
            'water': 'WLEAK',
            'water leak': 'WLEAK',
            'leak': 'WLEAK',
            'pipe': 'BPIPE',
            'burst': 'BPIPE',
            'electricity': 'ELEC',
            'power': 'ELEC',
        }
        
       
        db_code = search_map.get(query.lower())

        if db_code:
            
            faults = faults.filter(category__icontains=db_code)
        else:
         
            faults = faults.filter(
                Q(location_address__icontains=query) | 
                Q(description__icontains=query) |
                Q(category__icontains=query) |
                Q(ref_number__icontains=query)
            )

    return render(request, 'map/index.html', {'faults': faults})


def about(request): 
    return render(request, 'map/about.html')

def help_faq(request): 
    return render(request, 'map/help.html')

# This code ke ya the "I'm Affected" logic for residents to report that they are affected by a specific fault.
def im_affected(request):
    if request.method == 'POST':
        fault_id = request.POST.get('fault_id')
        name = request.POST.get('name')
        cellphone = request.POST.get('cellphone')

        try:
            incident = Fault.objects.get(id=fault_id)
            AffectedResident.objects.create(
                fault=incident,
                full_name=name,
                cellphone=cellphone
            )
            return JsonResponse({
                'status': 'success',
                'message': f'You have been added to report {incident.ref_number}'
            }, status=200)
        except Fault.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Incident not found'}, status=404)

    return JsonResponse({'status': 'invalid request'}, status=400)