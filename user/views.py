from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def index(request):
    return render(request, 'user/index.html')

def process(request):
    customer = Customer.objects.all()
    j='null'
    if request.method=="POST":
        email=request.POST['email']
        amt=request.POST['amount']
        rec=request.POST['rec']
        print(email)
        print(amt)
        print(rec)
        amt=int(amt)
        
        if email == 'select' or rec == 'select' or (email=='select' and rec=='select') or rec==email:
            messages.warning(request,"Email Id not selected or both Email Id's are same")  
        elif amt <= 0:
            messages.warning(request,'Please provide valid transfer amount!!')
        else:
            for c in customer:
                if c.email==email:
                    j=email
                    i=c.id
                    name=c.name
                    if amt > c.bal:
                        messages.warning(request,"Insufficient Balance!!")   
                    break

        for x in customer:
            if x.email==rec:
                rid=x.id
                rname=x.name
                rbal=x.bal
                break
 
        for c in customer: 
            if c.email==email and rec!=email and rec!='select' and amt<=c.bal and amt>0:
                q1= Transfer(sender=name,reciever=rname,amount=amt)
                bal=c.bal-amt
                q2= Customer.objects.filter(id=i).update(bal=bal)
                q1.save()
                bal=rbal+amt
                q3=Customer.objects.filter(id=rid).update(bal=bal)
                messages.success(request,"Transferred successfully!!")
                return redirect('transferdetails')
                
    return render(request,'user/transfermoney.html',{'customer':customer})

def transfer(request):
    tr = Transfer.objects.all()
    return render(request, 'user/transfer.html',{'tr':tr})

def details(request):
    customer = Customer.objects.all()
    return render(request,'user/customers.html',{'customer':customer})