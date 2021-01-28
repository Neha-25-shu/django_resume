from django.shortcuts import render

# Create your views here.
def skill(request):
    contaxt = {'skill': 'active'}
    return render(request,'education/skill.html',contaxt)
