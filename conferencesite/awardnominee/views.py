from django.shortcuts import render
from django.http import HttpResponseRedirect
from awardnominee.models import Awardnominee
from django.db.models import F
from django.urls import reverse


def awards(request):

    if request.method == 'POST':
        choice = request.POST.get('pollButton')
        nominee_list = Awardnominee.objects.all()

        for nominee in nominee_list:
            if nominee.nominee_name.split(' ',1)[0] == choice:
                nominee.num_votes += 1
                nominee.save()

    nominee_list = Awardnominee.objects.all()

    return render(request, 'awards.html', {'nominee_list': nominee_list})
