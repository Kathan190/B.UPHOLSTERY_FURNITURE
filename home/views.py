from django.shortcuts import render,HttpResponse
from home.models import Sofa
from home.models import Beds
from home.models import Chest
from home.models import Dining
from home.models import Dressing
from home.models import Wardrobs
from home.models import Index

# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        index = Index(name=name, subject=subject, message=message)
        index.save()
    return render(request, 'index.html')

def beds(request):
    beds = Beds.objects.all()
    context = {'beds':beds}
    return render(request, 'beds.html', context)

def chest(request):
    chest = Chest.objects.all()
    context = {'chest':chest}
    return render(request, 'chest.html', context)

def dining(request):
    dining = Dining.objects.all()
    context = {'dining':dining}
    return render(request, 'dining.html', context)

def dressing(request):
    dressing = Dressing.objects.all()
    context = {'dressing':dressing}
    return render(request, 'dressing.html', context)

def sofa(request):
    sofa = Sofa.objects.all()
    context = {'sofa':sofa}
    return render(request, 'sofa.html', context)

def wardrobs(request):
    wardrobs = Wardrobs.objects.all()
    context = {'wardrobs':wardrobs}
    return render(request, 'wardrobs.html', context)

