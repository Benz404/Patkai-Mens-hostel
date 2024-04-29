from unicodedata import name
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from main.models import students_detail
from comittee.models import fees_record
from django.contrib.auth.decorators import login_required


def login_user(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        messages.success(request,("wrong username or password !!! please try again"))
        return redirect('login')
    return render(request,'login.html')


@login_required
def superpage(request,*args, **kwargs):
    stored_data=students_detail.objects.all().order_by('room_number')
    dna_data={
        'dataline':stored_data,
    }
    return render(request,'superpage.html',dna_data)


def logout_user(request):
    logout(request)
    messages.success(request,("you are logged out !!!"))
    return redirect('/')


@login_required
def delete(request,pk):
  data_line = get_object_or_404(students_detail, pk=pk)
  data_link= fees_record.objects.filter(roll_number=data_line.roll_number)
  data_line.delete()
  data_link.delete()
  messages.success(request,("The data is deleted successfully"))
  return redirect('superpage')

@login_required
def delete_fees(request,pk):
    data_line = get_object_or_404(fees_record, pk=pk)
    data_line.delete()
    messages.success(request,("The data is deleted successfully"))
    return redirect('payment_students_list')

@login_required
def edit(request,pk):
    stored_data = get_object_or_404(students_detail, pk=pk)
    if request.method=="POST":
        name=request.POST.get('name')
        roll=request.POST.get('roll')
        wing=request.POST.get('wing')
        the_room=request.POST.get('room')
        department=request.POST.get('department')
        school=request.POST.get('school')
        phone=request.POST.get('phone')
        email=request.POST.get('mail')
        stored_data.students_name=name
        stored_data.roll_number=roll
        stored_data.department=department
        stored_data.School=school
        stored_data.room_number=the_room
        stored_data.wing_name=wing
        stored_data.phone_number=phone
        stored_data.email_id=email
        stored_data.save()
        return render(request,'success.html',{'confirmation':"Your data is Updated successfully !!!"})
    return render(request,'edit_detail.html',{'dataline':stored_data})


@login_required
def payment_student_list(request,*args, **kwargs):
    stored_data = students_detail.objects.all().order_by('room_number')
    return render(request,'payment_list.html',{'dataline':stored_data})


@login_required
def payment_form(request,pk):
    stored_data = get_object_or_404(students_detail, pk=pk)
    if request.method=="POST":
        this_year=request.POST.get('year')
        this_month=request.POST.get('month')
        transaction_no=request.POST.get('trid')
        dues=request.POST.get('fees_amount')
        fine=request.POST.get('fine_amount')
        dues=float(dues)
        fine=float(fine)
        total=dues+fine
        data=fees_record(student_name=stored_data.students_name,roll_number=stored_data.roll_number,room_number=stored_data.room_number,month=this_month,year=this_year,transaction_id=transaction_no,mess_dues=dues,fine_dues=fine,total_dues=total)
        data.save()
        return render(request,'success.html',{'confirmation':"fees record added successfully !!"})
    return render(request,'payment_form.html',{'dataline':stored_data})


@login_required
def fees_history(request,pk):
    stored_data = get_object_or_404(students_detail, pk=pk)
    all_data=fees_record.objects.filter(roll_number=stored_data.roll_number).order_by("-collected_time")
    context={
        'dataline':all_data,
        'parent_data':stored_data
    }
    return render(request,'fees_history.html',context)

@login_required
def visualisation(request,*args,**kwargs):
    if request.method=="POST":
        year_data=request.POST.get('year')
        month_data=request.POST.get('month')
        payers=fees_record.objects.filter(month=month_data,year=year_data).order_by('room_number')
        context={
         'dataline':payers,
         'year':year_data,
         'month': month_data
         }
        return render(request,'record_start.html',context)
    return render(request,'record_start.html')

@login_required
def reciept(request,pk):
    stored_data = get_object_or_404(fees_record, pk=pk)
    context={
        'dataline':stored_data
    }
    return render(request,'reciept.html',context)