from django.shortcuts import render ,HttpResponseRedirect
from .models import StudentModel
from .forms import StudentForm
# Create your views here.

#add and show function
def index(request):
    if request.method =='POST':
        fm = StudentForm(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            gd=fm.cleaned_data['grade']
            reg = StudentModel(name=nm,email=em,grade=gd)
            reg.save()
            fm = StudentForm()
        
    else:
        fm = StudentForm()
    stud=StudentModel.objects.all()
        
    return render(request,'myapp/addandshow.html',{'form':fm,
    'stu':stud,})

#delete function
def updae_data(request,id):
    if request.method == 'POST':
        pi = StudentModel.objects.get(pk=id)
        fm = StudentForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = StudentModel.objects.get(pk=id)
        fm = StudentForm(instance=pi)
    
    return render(request,'myapp/update.html',{'form':fm},)


def delete_data(request,id):
    if request.method =='POST':
        pi=StudentModel.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')