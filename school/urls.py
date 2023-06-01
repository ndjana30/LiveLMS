from . import views
from django.urls import path,include
from .views import StudentRegistrationView, view_courses_as_teacher, view_lessons, view_lessons_as_teacher, view_subjects,view_courses
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('<pk>/<slug:slug>/quiz_add/',views.add_quiz,name='add_quiz'),
    path('<pk>/<slug:slug>/take_quiz/',views.take_quiz,name='take_quiz'),
    path('<pk>/answer_quiz/',views.take_question_quiz,name='answer_quiz'),
    path('',views.starter_page,name='starter'),
    path('signup',StudentRegistrationView.as_view(),name='signup'),
    path('login/',views.login_user,name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('subjects/',view_subjects,name='view_subjects'),
    path('<pk>/courses/',view_courses,name='view_courses'),
    path('courses/',view_courses_as_teacher,name='view_courses_as_teacher'),
    path('courses/<pk>/<slug:slug>/lessons/',view_lessons_as_teacher,name='view_lessons_as_teacher'),
    path('courses/<pk>/<slug:slug>/',view_lessons,name='view_lessons'),
    path('lesson/create/',views.LessonCreateView,name='create'),
    path('<pk>/update/',views.LessonUpdateView,name='update'),
    path('<pk>/delete/',views.LessonDeleteView,name='delete'),
    path('lesson/live-class-room/',views.class_room_view,name='class_room'),
    path('<pk>/question_add/',views.add_question_to_quiz,name='add_question'),
    
    # path('lesson/<pk>/update/',LessonUpdateView,name='lesson_update'),
    # path('<pk>/update/',LessonFilesUpdateView,name='lesson_file_update'),
    ]
