from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
from pytz import timezone
import random as rand
# Create your models here.
class Subject(models.Model):
    ICT = 'ICT'
    BMS = 'BMS'
    choises=[
        (ICT,'ICT'),
        (BMS,'BMS'),
    ]
    name = models.CharField(max_length=250, blank=False,null=False)
    image = models.ImageField(upload_to='Images/sujects/', default = 'Images/django.jpg')
    department = models.CharField(choices=choises,default=ICT,max_length=250)
    slug=models.SlugField(max_length=250,blank=False)

  

    def __str__(self):
        return self.name+'\t' f'under the \t'+self.department+'\t department'

class Course(models.Model):
    name = models.CharField(max_length=250, blank=False,null=False)
    image = models.ImageField(upload_to='Images/courses/', default = 'Images/django.jpg')
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE,related_name='courses')
    slug=models.SlugField(max_length=250,blank=False)
    credit = models.PositiveIntegerField(default=3)
    Instructor = models.ForeignKey(User,on_delete=models.CASCADE,related_name='courses')
    
    def get_absolute_url(self):
        return reverse("school:add_quiz", args=[self.pk,self.slug])


    def __str__(self):
        return self.name

class Quiz(models.Model):
    name= models.TextField(max_length=250)
    course = models.ForeignKey(Course,related_name='quizes',on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created']
    
    def get_absolute_url(self):
        return reverse("school:add_question", args=[self.pk])

    def __str__(self):
        return self.name

class Question(models.Model):
    sentence = models.TextField(max_length=255)
    quiz = models.ForeignKey(Quiz,related_name='questions',on_delete=models.CASCADE)
    a =  models.TextField(max_length=255)
    b =  models.TextField(max_length=255)
    c =  models.TextField(max_length=255)
    d =  models.TextField(max_length=255)
    ans = models.TextField(max_length=250)

    def __str__(self):
        return self.sentence


class Medias(models.Model):
    video = models.FileField(blank=True,upload_to='videos/')
    file = models.FileField(blank=True,upload_to='Files/')
    image = models.ImageField(blank=True,upload_to='Images/')
    uploaded = models.DateField(auto_now_add=True)
    class Meta:
        abstract = True
        ordering = ['-uploaded']




class Lesson(Medias):
    name = models.CharField(max_length=250, blank=False,null=False)
    description = models.CharField(max_length=250, default="Hello short lesson description")
    slug=models.SlugField(max_length=250,blank=False)
    # quiz = models.OneToOneField(Quizs,on_delete=models.CASCADE, null=True,blank=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='lessons')

    class Meta:
        ordering = ['-course']

    def get_absolute_url(self):
        return reverse("school:view_lessons", args=[self.pk])
    
    def __str__(self):
        return self.name



class Profile(models.Model):
    name=models.CharField(max_length=250,blank=False)
    # matricule = models.PositiveIntegerField(default=rand.randint(0,999999))
    slug=models.SlugField(max_length=250,blank=False)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    photo = models.ImageField(upload_to ='users/%Y/%m/%d/',blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender,instance,created,**kwargs):
        if created:
            Profile.objects.create(user=instance)
    
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance , **kwargs):
        instance.profile.save()

    def __str__(self):
        return f'Profile for user {self.user.username}'

class LiveClassRoom(models.Model):
    course = models.ForeignKey(Course,related_name='live_class_room',on_delete=models.CASCADE)
    number = models.PositiveIntegerField(default=rand.randint(0,999999))