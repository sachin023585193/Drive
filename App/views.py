from django.http import JsonResponse
from django.shortcuts import render
from .models import Drive

# Create your views here.
def index(request):
    if request.method == 'POST' and request.FILES:
        Drive.objects.create(file=request.FILES['file'],name=request.POST['name'],size=request.POST['size'],extension=request.POST['extension'])
        return JsonResponse({'status':'success'})
    data = Drive.objects.all().order_by('-uploaded')
    context = {'files':data}
    return render(request,'index.html',context)