from django.shortcuts import render, get_object_or_404
from .models import KiTa

def kita_list(request):

    kitas = KiTa.objects.order_by('kita_name')

    return render(request, 'take_care_app/kita_list.html', {'kitas': kitas})

def kita_detail(request, pk):

    kita = get_object_or_404(KiTa, pk=pk)

    return render(request, 'take_care_app/kita_detail.html', {'kita': kita})