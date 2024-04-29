from django.db import models

# Create your models here.
class fees_record(models.Model):
    collected_time= models.DateTimeField(auto_now_add=True)
    student_name=models.CharField(default="",max_length=30)
    roll_number=models.CharField(default="",max_length=8)
    room_number=models.IntegerField(default=0)
    month=models.CharField(default="",max_length=10)
    year=models.IntegerField(default=2022)
    transaction_id=models.CharField(default="",max_length=30)
    mess_dues=models.DecimalField(default=0, max_digits=10, decimal_places=2)
    fine_dues=models.DecimalField(default=0, max_digits=10, decimal_places=2)
    total_dues=models.DecimalField(default=0, max_digits=10, decimal_places=2)
    def __str__(self):
        return (self.roll_number)