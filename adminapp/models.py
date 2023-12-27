from django.db import models
from django.db import connections
# Create your models here.



class Warehouse: 
    w_id: str 
    date: str
    brand_no : str
    brand_name : str
    size : str
    quantity_boxes : str 
    quantity_bottles : str



class Dailysheet(models.Model):

    d_id=models.IntegerField(primary_key=True) 
    date=models.DateField()
    brand_name=models.CharField(max_length=50)
    ML=models.IntegerField()
    Opening_bal	=models.IntegerField()
    plant=models.IntegerField()
    ob_total=models.IntegerField()
    Closing_bal=models.IntegerField()
    sales=models.IntegerField()
    MR=models.IntegerField()
    amount=models.IntegerField()
    class Meta:
        db_table="daily_sheet"
      
    
    
class Brands:
    bid:str
    brand_no:str
    brand_name:str 
    ML:str
    issue_price:str
    MRP:str

class Brand(models.Model):
    id=models.IntegerField(primary_key=True)
    brand_no=models.IntegerField()
    brand_name=models.CharField(max_length=50)
    ML=models.IntegerField()
    issue_price=models.IntegerField()
    MRP=models.IntegerField()
    class Meta:
        db_table="adminapp_brand"
    
class Dailysales:
    date : str
    retail_sale : str
    expenditure : str
    balance : str
    cashob : str
    total : str
    recash : str
    handcash : str
    
class Bills(models.Model):
    bill=models.FileField(null=True) 
    
class Employee:
    emp_id:str
    username:str
    email:str
    dob:str
    mobile:str

class Accountant:
    acc_id:str
    username:str
    email:str
    dob:str
    mobile:str
    



    



    

