from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import package, signupcred, logincred
# Create your views here.

def admin_login(requests):
    if requests.method == 'POST':
        username = requests.POST['username']
        password = requests.POST['password']
        user= authenticate(requests, username= username, password= password)
        if user is not None:
            login(requests, user)
            return redirect("admin_dashboard")
        else:
            error_message= "Invalid Username or Password"
            return render(requests, "adminlogin.html", {"error_message":error_message})
    return render(requests, 'adminlogin.html')

@login_required
def admin_logout(requests):
    logout(requests)
    return redirect("admin_login")
    

@login_required
def admin_dashboard(requests):
    data = package.objects.all()
    return render(requests, "admindashboard.html", {"data":data})

@login_required
def admin_add_package(requests):
    if requests.method== "POST":
        newpackage= package(
            Package_Description= requests.POST['package_info'],
            Quantity= requests.POST['quantity'],
            Weight= requests.POST['weight'],
            Package_Condition= requests.POST['condition'],
            Shipment_Status= requests.POST['status'],
            Shipping_Plan= requests.POST['shipment_plan'],
            Expected_Delivery_Date= requests.POST['delivery_date'],
            Dispatch_Date= requests.POST['dispatch_date'],
            Tracking_Id= requests.POST['tracking_id'],
            Shipment_Destination= requests.POST['shipment_destination'],
            Dispatch_Location= requests.POST['dispatch_location'],
            Current_Location= requests.POST['current_location'],
            Sender_FullName= requests.POST['sender_name'],
            Sender_Email= requests.POST['sender_email'],
            Sender_Contact= requests.POST['sender_number'],
            Sender_Address= requests.POST['sender_address'],
            Receiver_FullName= requests.POST['receiver_name'],
            Receiver_Email= requests.POST['receiver_email'],
            Receiver_Contact= requests.POST['receiver_number'],
            Receiver_Address= requests.POST['receiver_address'],
        )
        newpackage.save()
        return redirect('admin_dashboard')
    return render(requests, "addpackage.html", {})

@login_required
def admin_update_package(requests, id):
    packageinfo= get_object_or_404(package, id=id)

    if requests.method== "POST":
        packageinfo= get_object_or_404(package, id=id)
        
        packageinfo.Quantity= requests.POST['quantity']
        packageinfo.Weight= requests.POST['weight']
        packageinfo.Package_Condition= requests.POST['condition']
        packageinfo.Shipment_Status= requests.POST['status']
        packageinfo.Shipping_Plan= requests.POST['shipment_plan']
        packageinfo.Expected_Delivery_Date= requests.POST['delivery_date']
        packageinfo.Current_Location= requests.POST['current_location']
        
        packageinfo.save()
        return redirect('admin_dashboard')
    return render(requests, "updatepackage.html", {"packageinfo": packageinfo})

@login_required
def delete_package(requests, id):
    packageinfo= get_object_or_404(package, id=id)
    packageinfo.delete()

    return redirect("admin_dashboard")


def home(requests):
    #signup
    if requests.method== "POST":
        tracking_id= requests.POST['tracking_id']
        packageinfo= package.objects.get(Tracking_Id= tracking_id)
        return render(requests, "packageinfo.html", {"packageinfo": packageinfo})
        
    return render(requests, "index.html", {})


def signups(requests):
    if requests.method== "POST":    
        fullname= requests.POST['fullname']
        email= requests.POST['email']
        number= requests.POST['number']
        password= requests.POST['password']

        newusercred= signupcred(
            Fullname= fullname,
            Email= email, 
            Number= number,
            Password= password)
        newusercred.save()

        return redirect("home")
    
    return render(requests, "signup.html", {})

def logins(requests):
    if requests.method== "POST":
        email= requests.POST['email']
        password= requests.POST['password']

        usercred= logincred(
            Email= email,
            Password= password)
        usercred.save()

        return redirect("home")
    
    return render(requests, "login.html", {})