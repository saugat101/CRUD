from django.shortcuts import render,HttpResponsePermanentRedirect
from .forms import Studentegistration
from .models import User
from django.http import JsonResponse
# Create your views here.

#this function will add and show the data
def add_show(request):
    if request.method == 'POST':
        fm = Studentegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=User(name=nm,email=em,password=pw)
            reg.save()
            fm = Studentegistration()
            # return JsonResponse({"message": "User added successfully"})
    else:
        fm=Studentegistration()
    stud=User.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fm, 'stu':stud})

#this function will edit
def update_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm=Studentegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=Studentegistration(instance=pi)
    return render(request,'enroll/updatestudent.html',{'form':fm})


#this function will delete the data
def delete_data(request, id):
    if request.method == 'POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponsePermanentRedirect('/')