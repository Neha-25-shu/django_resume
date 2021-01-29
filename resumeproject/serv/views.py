from django.shortcuts import render

# Create your views here.


def services(request):
    contaxt = {'service': 'active'}
    return render(request, 'serv/services.html', contaxt)
