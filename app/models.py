from django.db import models
 
class Aadhar(models.Model):
    aadhar=models.IntegerField(unique=True)
    create_by=models.CharField(max_length=100)
    alloted_date=models.DateField()
    
# def __str__(self):
#         return str(self.aadhar)
    
    
class citizan(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    contect=models.IntegerField()
    aadhar_no=models.ForeignKey(Aadhar, on_delete=models.PROTECT,to_field='aadhar')
    
    
    def __str1__(self):
        return str(self.aadhar_no)
    

# Create your models here.
