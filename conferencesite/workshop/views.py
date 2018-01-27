from django.shortcuts import render
from workshop.models import Workshop

def workshop(request):

    workshop_list = Workshop.objects.all()

    return render(request, 'workshopschedule.html', {'workshop_list': workshop_list})
