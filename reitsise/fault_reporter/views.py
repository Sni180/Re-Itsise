from django.shortcuts import render
from django.http import JsonResponse
from .forms import FaultReportForm # Double check this name in forms.py

def report(request):
    if request.method == 'POST':
        form = FaultReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

    # FIX: This handles the initial page load (GET request)
    form = FaultReportForm()
    # Path must match your explorer: templates/fault_reporter/report.html
    return render(request, 'fault_reporter/report.html', {'form': form})