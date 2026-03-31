from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q 
from .models import Fault, AffectedResident 

# 1. The Main Map / Search View
def explorer_map(request):
    query = request.GET.get('search', '').strip()
    faults = Fault.objects.all().order_by('-date_reported')

    if query:
        # Create a mapping for common search terms to your DB codes
        search_map = {
            'water': 'WLEAK',
            'water leak': 'WLEAK',
            'leak': 'WLEAK',
            'pipe': 'BPIPE',
            'burst': 'BPIPE',
            'electricity': 'ELEC',
            'power': 'ELEC',
        }
        
        # Check if the user's word is in our map (case-insensitive)
        db_code = search_map.get(query.lower())

        if db_code:
            # If we found a code, search for that specific code
            faults = faults.filter(category__icontains=db_code)
        else:
            # Otherwise, perform the standard general search
            faults = faults.filter(
                Q(location_address__icontains=query) | 
                Q(description__icontains=query) |
                Q(category__icontains=query) |
                Q(ref_number__icontains=query)
            )

    return render(request, 'map/index.html', {'faults': faults})

# 2. The About View (The one currently missing)
def about(request): 
    return render(request, 'map/about.html')

# 3. The Help/FAQ View (The other one currently missing)
def help_faq(request): 
    return render(request, 'map/help.html')

# 4. The "I'm Affected" Logic
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