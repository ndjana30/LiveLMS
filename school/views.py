from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin)
from .models import LiveClassRoom,Subject,Course,Lesson,Profile
from .models import Question, Quiz

from .forms import LessonCreateForm, LessonUpdateForm,addQuestionform
from django.core.files.storage import FileSystemStorage
import os

# Create your views here.

#for all users
def starter_page(request):
    return render(request,'school/starter.html')

#for simple users and admin(superuser)
@login_required
def view_subjects(request):
    subject = Subject.objects.all()
    return render(request, 'school/home.html',{'subject':subject})


@login_required
def view_courses(request,pk):
    subject= Subject.objects.get(pk=pk)
    courses = subject.courses.all()

    instructor=request.user.courses.all() #with this, the instructor will view only what he created
    
    return render(request,'school/course_list.html',{'courses':courses,'instructor':instructor})

@login_required
def view_lessons(request,pk,slug):
    course = Course.objects.get(pk=pk,slug=slug)
    lessons=course.lessons.all()
    return render(request,'school/lessons_list.html',{'lessons':lessons,'course':course})

class StudentRegistrationView(CreateView):
    template_name='school/forms/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('view_subjects')

    def form_valid(self,form):
        result = super().form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username=cd['username'] , password=cd['password1'])
        login(self.request,user)
        return result

def LessonCreateView(request):
    
    if request.method == 'POST':
        form = LessonCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_subjects')
    else:
        form = LessonCreateForm()
    return render(request,'school/lesson/create_lesson.html',{'form':form})

@user_passes_test(lambda u: u.groups.filter(name='TEACHERS'))
@login_required
def LessonUpdateView(request,pk):
    lesson = Lesson.objects.get(pk=pk)
    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(lesson.image) > 0: 
                os.remove(lesson.image.path)
            lesson.image = request.FILES['image']
            if len(lesson.file) > 0:
                os.remove(lesson.file.path)
            lesson.file = request.FILES['file']
            if len(lesson.video) > 0:
                os.remove(lesson.video.path)
            lesson.video = request.FILES['video']
        lesson.image = request.FILES['image']
        lesson.file = request.FILES['file']
        lesson.name = request.POST.get('name')
        lesson.video = request.FILES['video']
        lesson.description = request.POST.get('description')
        lesson.save()
        return redirect('/')
    return render(request,'school/lesson/update_lesson.html',{'lesson':lesson})
        
@login_required
@user_passes_test(lambda u: u.groups.filter(name='TEACHERS'))
def LessonDeleteView(request,pk):
    lesson = Lesson.objects.get(pk=pk)
    lesson.delete()
    return redirect('view_subjects')

#for instructors
@login_required
@user_passes_test(lambda u: u.groups.filter(name='TEACHERS'))
def view_courses_as_teacher(request):
    courses=request.user.courses.all() #with this, the instructor will view only what he created
    return render(request,'school/lesson/instructor_course_list.html',{'courses':courses})

@login_required
@user_passes_test(lambda u: u.groups.filter(name='TEACHERS'))
def view_lessons_as_teacher(request,pk,slug):
    course = request.user.courses.get(pk=pk,slug=slug)
    lessons = course.lessons.all()

    return render(request,'school/lesson/instructor_lesson_list.html',{'lessons':lessons,'course':course})


@login_required
@user_passes_test(lambda u: u.groups.filter(name='TEACHERS'))
def class_room_view(request):
    return render(request,'school/class_room.html')
 
def login_user(request):
    if request.method == 'POST':
        user = authenticate(request,username=request.POST.get('name'),password = request.POST.get('password'))
        if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('/')
    return render(request,'registration/login.html')

from django.forms import modelformset_factory
# @login_required
# @user_passes_test(lambda u: u.groups.filter(name='TEACHERS'))
# def addQuestion(request):
#     quiz = Quizs.objects.all()
#     quiz_formset = modelformset_factory(Quizs,fields=('question','A','B','C','D','ans'),extra=9)
#     form=quiz_formset()
#     if request.method == 'POST':
#         form=quiz_formset(request.POST)
#         form.save()
#         # quiz=Quizs(question=request.POST.get('question'),
#         # user = request.user,
#         # A=request.POST.get('A'),
#         # B=request.POST.get('B'),
#         # C=request.POST.get('C'),
#         # D=request.POST.get('D'),
#         # ans=request.POST.get('ans'))
#         # quiz.save()
#         return redirect('/')
#     return render(request,'school/exam/quizz_create.html',{'quiz':quiz,'form':form})


@login_required
def take_quiz(request,pk,slug):
    course = Course.objects.get(pk=pk,slug=slug)
    quiz = course.quizes.all()
    return render(request,'school/exam/quizz.html',{'quiz':quiz})

@login_required
def take_question_quiz(request,pk):
    quiz = Quiz.objects.get(pk=pk)
    qtns = quiz.questions.all()
    return render(request,'school/exam/take_quiz.html',{'qtns':qtns})


@login_required
@user_passes_test(lambda u: u.groups.filter(name='TEACHERS'))
def add_quiz(request,pk,slug):
    course = Course.objects.get(pk=pk,slug=slug)
    qz = course.quizes.all()
    quiz = Quiz()
    quiz.course = course
    if request.method=='POST':
        quiz.name = request.POST.get('name')
        quiz.course = course
        quiz.save()
    return render(request, 'school/exam/quizz_create.html',{'quiz':quiz,'qz':qz})

@login_required
@user_passes_test(lambda u: u.groups.filter(name='TEACHERS'))
def add_question_to_quiz(request,pk):
    quiz=Quiz.objects.get(pk=pk)
    qstns = quiz.questions.all()
    n_qstns = qstns.count()
    question = Question()
    question.quiz=quiz
    if request.method=='POST':
        question.sentence=request.POST.get('sentence')
        question.quiz = quiz
        question.a=request.POST.get('a')
        question.b=request.POST.get('b')
        question.c=request.POST.get('c')
        question.d=request.POST.get('d')
        question.ans=request.POST.get('ans')
        question.save()
    return render(request,'school/exam/question_add.html',{'quiz':quiz,'question':question,'qstns':qstns,'n_q':n_qstns})


#  if request.method == 'POST':
#         print(request.POST)
#         course = Course.objects.get(pk=pk,slug=slug)
#         questions = course.mcqs.all()
#         score =0
#         wrong=0
#         correct=0
#         total=0
#         for q in questions:
#             total+=1
#             print(request.POST.get(q.question))
#             print(q.ans)
#             print()
#             if q.ans == request.POST.get(q.question):
#                 score+=10
#                 correct+=1
#             else:
#                 wrong=wrong+1
#         percent = score/(total*10) *100
#         context={
#             'score':score,
#             'time':request.POST.get('timer'),
#             'correct':correct,
#             'wrong':wrong,
#             'percent':percent,
#             'total':total

#         }
#         return render(request,'school/exam/result.html',context)
#     else:
