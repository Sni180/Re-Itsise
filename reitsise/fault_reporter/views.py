from django.shortcuts import render
from django.http import JsonResponse
from .forms import FaultReportForm 

def report(request):
    if request.method == 'POST':
        form = FaultReportForm(request.POST, request.FILES)
        
        if form.is_valid():
           
            fault = form.save(commit=False)
            
            
            fault.full_name = request.POST.get('full_name')
            fault.cellphone = request.POST.get('cellphone')
            fault.description = request.POST.get('description')
            
           
            fault.save() 
            
            return JsonResponse({'status': 'success'})
        
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

    form = FaultReportForm()
    return render(request, 'fault_reporter/report.html', {'form': form})