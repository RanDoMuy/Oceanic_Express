from django.db import models
# Create your models here.

class package(models.Model):
    Package_Description= models.CharField(("Package Description"), max_length=50)
    Quantity= models.IntegerField(("Quantity"))
    Weight= models.IntegerField(("Package Weight"))
    Package_Condition= models.CharField(("Package Condition"), max_length=50)

    Sender_FullName= models.CharField(("Sender Fullname"), max_length=50)
    Sender_Email= models.EmailField(("Sender Email Address"), max_length=20)
    Sender_Address= models.CharField(("Sender Address"), max_length=50)
    Sender_Contact= models.CharField(("Sender Contact"), max_length=11)

    Receiver_FullName= models.CharField(("Receiver Fullname"), max_length=50)
    Receiver_Email= models.EmailField(("Receiver Email address"), max_length=20)
    Receiver_Address= models.CharField(("Receiver Address"), max_length=50)
    Receiver_Contact= models.CharField(("Receiver Contact"), max_length=11)

    Shipping_Plan= models.CharField(("Shipping Plan"), max_length=50)
    Shipment_Status= models.CharField(("Shipment Status"), max_length=50)
    Shipment_Destination= models.CharField(("Shipment Destination"), max_length=50)
    Current_Location= models.CharField(("Current Package Location"), max_length=50)
    Dispatch_Date= models.DateField(("Dispatch Date"), auto_now=False, auto_now_add=False)
    Dispatch_Location= models.CharField(("Dispatch Location"), max_length=50)    
    Expected_Delivery_Date= models.DateField(("Expected Delivery Date"), auto_now=False, auto_now_add=False)
    Tracking_Id= models.CharField(("Tracking ID"), max_length=10)

    def __str__(self):
        return self.Receiver_FullName

class signupcred(models.Model):
    Fullname= models.CharField(("Fullname"), max_length=50)
    Number= models.IntegerField(("Phone Number"))
    Email= models.EmailField(("Email Address"), max_length=50)
    Password= models.CharField(("Password"), max_length=50)

    def __str__(self):
        return self.Fullname
    
class logincred(models.Model):
    Email= models.EmailField(("Email Address"), max_length=50)
    Password= models.CharField(("Password"), max_length=50)

    def __str__(self):
        return self.Email