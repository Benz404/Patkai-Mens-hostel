from ast import And
from django.shortcuts import render,get_object_or_404,redirect
from main.models import students_detail
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def author(request):
    return render(request,'author.html')

def students_list(request,*args, **kwargs):
    stored_data=students_detail.objects.all().order_by('room_number')
    return render(request,'students.html',{'data':stored_data})

def the_student(request,pk):
  data = get_object_or_404(students_detail, pk=pk)
  return render(request, "students_detail.html", {'data':data})

def students_admit_form(request,*args, **kwargs):
    if request.method=="POST":
        name=request.POST.get('name')
        roll=request.POST.get('roll')
        phone=request.POST.get('phone')
        department=request.POST.get('department')
        school=request.POST.get('school')
        room=request.POST.get('room')
        wing=request.POST.get('wing')
        email=request.POST.get('email') 
        if students_detail.objects.filter(roll_number=roll).exists() and students_detail.objects.filter(phone_number=phone).exists():
            messages.success(request,("This roll number or phone number is already exist in the database"))
            return redirect('students_admit_form')
        data=students_detail(students_name=name,roll_number=roll,room_number=room,department=department,wing_name=wing,email_id=email,phone_number=phone,School=school)
        data.save()
        return render(request,'success.html',{'confirmation':"Your data is submitted successfully !!!"})
    return render(request,'students_admit_form.html')