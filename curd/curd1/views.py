from django.shortcuts import render,HttpResponse,redirect

from curd1.forms import Studentform
from curd1.models import Student

# Create your views here.
def login(request):
    if request.method=="POST":
       
        form=Studentform(request.POST)
        try:
           if form.is_valid():
            form.save()
            return redirect("/show")
        except:
                 return HttpResponse("jjjjj") 
    else:
        form=Studentform()
    return render(request,'login.html',{'form':form}) 
def show(request):
    form=Student.objects.all()
    return render(request,'show.html',{'form':form})
def edit(request,id):
    form=Student.objects.get(id=id)
    return render(request,'edit.html',{'form':form})
def update(request,id):
    form=Student.objects.get(id=id)
    if request.method=="POST":
        d=Studentform(request.POST,instance=form)
        d.save()
        return redirect('/show')
def delete(request,id):
    form=Student.objects.get(id=id)
    form.delete()
    return redirect('/show')
        
        
    
   
                        
