from django.shortcuts import render,HttpResponse
from home.models import Sofa
from home.models import Beds
from home.models import Chest
from home.models import Dining
from home.models import Dressing
from home.models import Wardrobs

# Create your views here.
def index(request):
    return render(request, 'index.html')

def beds(request):
    beds = Beds.objects.all()
    context = {'beds':beds}
    return render(request, 'beds.html', context)

def chestofdrawer(request):
    return render(request, 'chestofdrawer.html')

def diningtable(request):
    return render(request, 'diningtable.html')

def dressingtable(request):
    return render(request, 'dressingtable.html')

def sofa(request):
    sofa = Sofa.objects.all()
    context = {'sofa':sofa}
    return render(request, 'sofa.html', context)

def wardrobs(request):
    return render(request, 'wardrobs.html')

