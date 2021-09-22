from django.shortcuts import render,HttpResponse
from .models import Task,task2
from django.shortcuts import redirect

# Create your views here.
def home(request):
    if(request.method == "POST"):
        title=request.POST.get('task')
        description=request.POST.get('dis')
        date = request.POST.get('birthday')

        savedata=task2(tasktitle=title,taskdes=description,taskdate=date)
        savedata.save()

        

        
    return render(request,'home.html')
    

def task(request):
    # alltask = task2.objects.all()
    data = task2.objects.all()

    return render(request,'task.html',{'data':data})  

def delete(request, id):
    task2.objects.filter(id=id).delete()

    return redirect('task')


def about(request):

    return render(request,'about.html')   