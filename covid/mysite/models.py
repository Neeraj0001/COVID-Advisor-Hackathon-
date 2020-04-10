from django.db import models

# Create your models here.
class meter_data(models.Model):
    s_no=models.CharField(max_length=10,default="")
    country_name=models.CharField(max_length=10,default="")
    no_patient=models.CharField(max_length=10,default="")
    death=models.CharField(max_length=10,default="")
    no_recovered=models.CharField(max_length=10,default="")
    def __str__(self):
        return self.s_no
class helpline_data(models.Model):
    s_no=models.CharField(max_length=20,default="")
    State_name=models.CharField(max_length=20,default="")
    Helpline_no=models.CharField(max_length=20,default="")
 
    def __str__(self):
        return self.State_name
class donation_data(models.Model):
    
    Full_name=models.CharField(max_length=20,default="")
    Phone_no=models.CharField(max_length=20,default="")
    City=models.CharField(max_length=20,default="")
    State=models.CharField(max_length=20,default="")
    Zip=models.CharField(max_length=20,default="")
    Address=models.CharField(max_length=50,default="")
    Donation=models.CharField(max_length=500,default="")

 
    def __str__(self):
        return self.Full_name

class news_data(models.Model):
    s_no=models.AutoField
    heading=models.CharField(max_length=100,default="")
    image=models.ImageField(upload_to='pics',default="")
    newsdata=models.TextField(default="")

