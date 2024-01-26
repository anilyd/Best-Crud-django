from django.db import models

# Create your models here.
class Employee(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,default="anil")
    phone=models.CharField(max_length=50,default="9335543724")

def __str__(self):
    return str(self.id)+""+self.name

