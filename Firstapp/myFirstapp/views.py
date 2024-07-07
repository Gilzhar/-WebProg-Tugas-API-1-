import sys
from django.contrib import messages
from django.db.models.signals import post_save
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q
from django.contrib.auth.models import User
from myFirstapp.models import AccountUser, Course, AttendingCourse
from myFirstapp.signals import check_nim
from myFirstapp.forms import StudentRegisterForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def readCourse(request):
    data = Course.objects.all()[:1]  # limit data (1 pcs)
    context = {'data_list': data}
    return render(request, 'course.html', context)

@csrf_protect
def createCourse(request):
    if request.method == 'POST':
        # Handle course creation logic here
        pass
    return render(request, 'home.html')

@csrf_protect
def updateCourse(request):
    if request.method == 'POST':
        # Handle course update logic here
        pass
    return render(request, 'home.html')

@csrf_protect
def deleteCourse(request):
    if request.method == 'POST':
        # Handle course deletion logic here
        pass
    return render(request, 'home.html')

def readStudent(request):
    data = AccountUser.objects.all()
    context = {'data_list': data}
    return render(request, 'index.html', context)

@csrf_protect
def createStudent(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            post_save.disconnect(check_nim)
            new_student = form.save(commit=False)
            new_student.account_user_created_by = request.user.username
            new_student.save()
            post_save.send(sender=AccountUser, created=True, instance=new_student, dispatch_uid="check_nim")
            messages.success(request, 'Data Berhasil disimpan')
            return redirect('myFirstApp:read-data-student')
    else:
        form = StudentRegisterForm()
    return render(request, 'form.html', {'form': form})

@csrf_protect
def updateStudent(request, id):
    student = get_object_or_404(AccountUser, account_user_id=id)
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil disimpan')
            return redirect('myFirstApp:read-data-student')
    else:
        form = StudentRegisterForm(instance=student)
    return render(request, 'form.html', {'form': form})

@csrf_protect
def deleteStudent(request, id):
    student = get_object_or_404(AccountUser, account_user_id=id)
    user = get_object_or_404(User, username=student.account_user_related_user)
    student.delete()
    user.delete()
    messages.success(request, 'Data Berhasil dihapus')
    return redirect('myFirstApp:read-data-student')
