from . import models
from django import forms

class News_form(forms.ModelForm):
    class Meta:
        model = models.News
        fields = [
            'title',
            'text',
            'picture',
            'writer',  
        ]
        widgets = {
            'picture': forms.ClearableFileInput(attrs={'id': 'article_picture'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # دریافت یوزر از ویو
        super().__init__(*args, **kwargs)
        if user:
            self.fields['writer'].initial = user.username

class Teacher_form(forms.ModelForm):
    class Meta:
        model = models.Teacher
        fields = [
            'name',
            'lastname',
            'title',
            'description',
            'file',
        ]
        widgets = {
            'file': forms.ClearableFileInput(attrs={'id': 'lesson_file'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # دریافت یوزر از ویو
        super().__init__(*args, **kwargs)
        if user:
            self.fields['name'].initial = user.username

class Student(forms.ModelForm):
    class Meta:
        model = models.Students
        fields = [
            'first_name',
            'phone',
            'description',
            'class_name',



        ]



