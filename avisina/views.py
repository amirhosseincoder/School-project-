from django.shortcuts import render, redirect,get_object_or_404
from .forms import Teacher_form , News_form,Student
import jdatetime
from django.utils import timezone
from . import models
from django.contrib.auth import authenticate,login
from .forms import News_form, Teacher_form
from django.contrib import messages


def home(request):
    chap=models.News.objects.all()
    return render(request,'index.html',{'chap':chap})

def error(request):
    return render(request,'error.html')

def blog_detail(request,item_id):
    text=get_object_or_404(models.News,id=item_id)
    #برای تبدیل تاریخ میلادی به شمسی و نمایش آن
    now_local=timezone.localtime(timezone.now())
    now_j=jdatetime.datetime.fromgregorian(datetime=now_local)
    
    
    date = now_j.strftime('%Y/%m/%d')
    time = now_j.strftime('%H:%M:%S')
    return render(request,'page.html',{'text':text,'date':date,'time':time})



def questions(request):
    pdf=models.Teacher.objects.all()
    return render(request,'question.html',{
        'pdf':pdf
    })
    

    
     
def teacher(request):
    if request.method == 'POST':
        form = Teacher_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
 
    else:
        form = Teacher_form()
    
    return render(request, 'teacher-action.html', {'form': form})


def news(request):
    if request.method == 'POST':
        form = News_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')  
    else:
        form = Teacher_form()
    
    return render(request, 'blog-detail.html', {'form': form})



def student(request):
    classes=models.Classes.objects.all()
    if request.method == 'POST':
        form = Student(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'دانش آموز گرامی درخواست شما ثبت و مشاور ما در اسرع وقت با شما ارتباط خواهد گرفت')
            return redirect('avisina:home')
            
        else:
            return redirect('avisina:erros')
    else:
        form = Teacher_form()
    
    return render(request, 'form_students.html', {'form': form,'classes':classes})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # login باید قبل از redirect انجام شود

            if user.is_staff:#برای فعال کردن این قسمت میتوانیم برویم در پنل ادمین در قسمت یوزر <ایز استف> کاربر را فعال کنیم
                messages.success(request, 'ورود موفقیت‌آمیز بود (پنل معلم)', extra_tags='site')#برای نمایش بهتر  پیام ها extra_tag استفاده میکنیم از
                return redirect("avisina:teacher_dashboard")
            else:#و اگر نبود به عنوان دانش آموز(کاربر عادی) میشناسه
                messages.success(request, 'ورود موفقیت‌آمیز بود', extra_tags='site')
                return redirect("avisina:home")

        else:
            messages.error(request, 'نام کاربری یا رمز عبور اشتباه است', extra_tags='site')
            return redirect("avisina:login")

    return render(request, "login.html")




def teacher_dashboard(request):
    print(request.POST)
    print(request.FILES)
    lesson_form = Teacher_form(user=request.user)
    article_form = News_form(user=request.user)
#در اینجا تمامی فرم ها در یک تابع استفاده شده است
    if request.method == 'POST':
        if 'submit_lesson' in request.POST:
            lesson_form = Teacher_form(request.POST, request.FILES, user=request.user)
            if lesson_form.is_valid():
                lesson_form.save()
                messages.success(request, 'آپلود موققیت امیز بود', extra_tags='site')
                return redirect('avisina:teacher_dashboard')
            else:
                messages.success(request, 'مشکلی وجود دارد', extra_tags='site')

        elif 'submit_article' in request.POST:
            article_form = News_form(request.POST, request.FILES, user=request.user)
            if article_form.is_valid():
                article_form.save()
                messages.success(request, 'آپلود موققیت امیز بود', extra_tags='site')
                return redirect('avisina:teacher_dashboard')
            else:
                messages.success(request, 'مشکلی وجود دارد', extra_tags='site')

    context = {
        'lesson_form': lesson_form,
        'article_form': article_form,
    }

    return render(request, 'teachers.html', context)

#document.addEventListener('DOMContentLoaded', () => {
#  setupUpload('lessonUploadTrigger', 'lesson_file');
#  setupUpload('articleUploadTrigger', 'article_file');
#});

def message(request):
    mess=models.Students.objects.all()
    return render(request,'inspect.html',{'mess':mess})


def about(request):
    return render(request,'about.html')



