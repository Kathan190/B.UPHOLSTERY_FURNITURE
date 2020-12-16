from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def beds(request):
    return render(request, 'beds.html')

def chestofdrawer(request):
    return render(request, 'chestofdrawer.html')

def diningtable(request):
    return render(request, 'diningtable.html')

def dressingtable(request):
    return render(request, 'dressingtable.html')

def sofa(request):
    return render(request, 'sofa.html')

def wardrobs(request):
    return render(request, 'wardrobs.html')

