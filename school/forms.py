from django import forms
from .models import Lesson,Medias

class LessonUpdateForm(forms.ModelForm):
    class Meta:
        model=Lesson
        fields = ('name','course','video','file','image')

# class LessonMediaUpload(forms.ModelForm):
#     class Meta:
#         model = Medias
#         fields =('name','video','lesson','file','image')

class LessonCreateForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ('name','course','video','file','image')

class addQuestionform(forms.ModelForm):
    class Meta:
        # model=Quizs
        fields="__all__"

