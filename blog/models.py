from django.db import models
from django.contrib.auth.models import User
# Create your models here.
import datetime
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.utils import timezone
from django.urls import reverse


class profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    slug =models.SlugField(null=True , blank=True)
    email=models.CharField(blank=True , max_length=100)
    

def save(self , *args , **kwargs):
    if not self.slug:
        self.slug = slugify(self.user)
    super(profile , self).save( *args , **kwargs)

    def __str__(self):  # part2 10:00
        return self.first_name


def CProfile(sender , **kwargs):
    if kwargs['created']:
        user_profile = profile.objects.create(user=kwargs['instance'])

post_save.connect(CProfile, sender=User)
 
 
 #########  اضافة سؤال #########


class post(models.Model):
    title= models.CharField(max_length=100)
    text1= models.TextField(max_length=1000)
    postDate =models.DateTimeField(default=timezone.now , null=True , blank=True)
    phone_number = models.CharField(max_length=11,null=True , blank=True)
    userD= models.ForeignKey(User, on_delete=models.CASCADE) #هذا اذا اليوزر انحذف ينحذف الجدول
    img = models.ImageField(upload_to ='pics' , null=True , blank=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('newAccount/' , args=[self.pk])
    class Meta:
        ordering = ('-postDate',)


class comment(models.Model):
    name = models.CharField(max_length=100)
    text2 = models.TextField(max_length=2000)
    comT =models.DateTimeField(default=timezone.now , null=True , blank=True)
    post = models.ForeignKey(post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.name



















