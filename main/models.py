from django.db import models

# Create your models here.
class students_detail(models.Model):
    created_time= models.DateTimeField(auto_now_add=True)
    students_name=models.CharField(default="",max_length=25)
    roll_number=models.CharField(default="",max_length=8)
    room_number=models.IntegerField(default=0)
    department=models.CharField(default="",max_length=30)
    wing_name=models.CharField(default="",max_length=20)
    email_id=models.EmailField(default="",max_length=30)
    phone_number=models.IntegerField(default=0)
    School=models.CharField(default="",max_length=25)
    def __str__(self):
        return (self.students_name)