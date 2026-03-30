from django.shortcuts import render
from .models import Fault

def explorer_map(request):
    # Fetch all reports to display on the map and in the activity list
    faults = Fault.objects.all().order_by('-date_reported')
    
    # The 'icon' property is handled automatically by the Fault model logic
    return render(request, 'map/index.html', {'faults': faults})

def about(request): return render(request, 'about.html')
def help_faq(request): return render(request, 'help.html')

from django.http import JsonResponse
from .models import Fault  

def im_affected(request):
    if request.method == 'POST':
        fault_id = request.POST.get('fault_id')
        name = request.POST.get('name')
        cellphone = request.POST.get('cellphone')

        try:
            # 1. Find the incident in your database
            incident = Fault.objects.get(id=fault_id)
            
            # 2. Logic: You can log this to a new model or just increment a count
            # For now, we'll just return a success message to trigger your modal
            return JsonResponse({'status': 'success'}, status=200)
            
        except Fault.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Incident not found'}, status=404)

    return JsonResponse({'status': 'invalid request'}, status=400)