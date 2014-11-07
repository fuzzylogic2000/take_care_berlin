from django.shortcuts import render
from .models import KiTa

def kita_list(request):

    kitas = KiTa.objects.order_by('kita_name')

    return render(request, 'take_care_app/kita_list.html', {'kitas': kitas})