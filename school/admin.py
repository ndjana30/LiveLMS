from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Subject)
class SubjectModel(admin.ModelAdmin):
    prepopulated_fields  = {'slug':(['name'])}

@admin.register(Course)
class CourseModel(admin.ModelAdmin):
    prepopulated_fields  = {'slug':(['name'])}

@admin.register(Lesson)
class LessonModel(admin.ModelAdmin):
    prepopulated_fields  = {'slug':(['name'])}

@admin.register(Profile)
class ProfileModel(admin.ModelAdmin):
    prepopulated_fields = {'slug':(['name'])}

admin.site.register(LiveClassRoom)
admin.site.register(Question)
admin.site.register(Quiz)
# admin.site.register(Quizs)
