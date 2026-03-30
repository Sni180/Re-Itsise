from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Fault, AffectedResident # Make sure both are imported

def explorer_map(request):
    # This powers your main Kimberley map and the recent activity sidebar
    faults = Fault.objects.all().order_by('-date_reported')
    return render(request, 'map/index.html', {'faults': faults})

def about(request): return render(request, 'about.html')
def help_faq(request): return render(request, 'help.html')

def im_affected(request):
    if request.method == 'POST':
        fault_id = request.POST.get('fault_id')
        name = request.POST.get('name')
        cellphone = request.POST.get('cellphone')

        try:
            # 1. Find the specific fault they are joining
            incident = Fault.objects.get(id=fault_id)
            
            # 2. CREATE the record in the AffectedResident table
            # This is what makes the entry show up in your Admin "Inlines"
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