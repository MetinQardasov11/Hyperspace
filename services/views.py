from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Service

def services(request):
    services = Service.objects.all()
    
    context = {
        'services': services
    }
    
    return render(request, 'services/services.html', context)


def service_detail(request, service_slug):
    
    service = get_object_or_404(Service, slug=service_slug)
    
    context = {
        'service': service
    }
    
    return render(request, 'services/service-details.html', context)