from django.shortcuts import render,redirect
from .models import Employee
# Create your views here.
def home(request):
    return render(request,"index.html")
def contact(request):

    eobj=Employee.objects.all()
    # detail={"name":"anil","Designation":"python developer"}
    return render(request,"contact.html",{"data":eobj})

def deleteb(request,id):
    dobj=Employee.objects.get(id=id)
    print("dobj------------------",dobj)
    if dobj:
        dobj.delete()
        return redirect("/contact/")
    return render(request,"contact.html")
def updatef(request,id):
    dp=Employee.objects.get(id=id)
    if request.method=="POST":     
        dp.name=request.POST.get("name")
        dp.phone=request.POST.get("phone")
        dp.save()
        return redirect("/contact/")
    return render(request,"update.html",{'d':dp})
def addf(request):
    data=Employee()
    if request.method=="POST":
        data.name=request.POST.get("name")
        data.phone=request.POST.get("phone")
        data.save()
        return redirect("/contact/")
    return render(request,"add.html")