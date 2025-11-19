from django.urls import path
from . import views

app_name="avisina"

urlpatterns = [
    path('blog_detail/<int:item_id>',views.blog_detail,name="blog_detail"),
    path('questions/',views.questions,name="questions"),
    path('messages/',views.error,name="errors"),
    path('student/',views.student,name="student"),
    path('login/',views.login_view,name="login"),
    path('',views.home,name="home"),
    path('aboute/',views.about,name="about"),
    path('message/',views.message,name="message"),
    path('teacher_dashboard/',views.teacher_dashboard,name="teacher_dashboard"),
    #path('news/',views.news,name="news"),
    #path('create_class/',views.create_class,name="create_class"),
]