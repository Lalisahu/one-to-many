from django.db import models
 
class Aadhar(models.Model):
    aadhar=models.IntegerField()
    create_by=models.CharField(max_length=100)
    alloted_date=models.DateField()
    
class citizan(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    contect=models.IntegerField()
    aadhar_no=models.ForeignKey(Aadhar, on_delete=models. PROTECT)

# Create your models here.
