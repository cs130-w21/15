from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.db.models.signals import post_save
from django.utils.text import slugify
from django.dispatch import receiver
import uuid
from nlp.word_cloud import plot_word_cloud
# import uuid
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    #snippet = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    header_image =  models.ImageField(null=True, blank=True, upload_to='images/')
    content = models.TextField(default="")
    # content = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    post_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    likes = models.ManyToManyField(User, related_name='blogs')

    class Meta:
        ordering = ['-created_on']

    def get_total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + "-" + self.post_id.urn

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
        plot_word_cloud(self.content, './blog/static/img/' + self.title)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(null=True, default="I have not write anything about myself yet")
    profile_pic = models.ImageField(null=True, blank=True, upload_to='images/profile', default=None)
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return str(self.user)


class Page(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.URLField()
    width = models.IntegerField()
    height = models.IntegerField()


class HeatMap(models.Model):
    '''This model stores the mouse coordinates'''
    name = models.TextField(primary_key=True)
    x_coord = models.TextField(blank=False, null=False)
    y_coord = models.TextField(blank=False, null=False)
    url = models.ForeignKey(Page, on_delete=models.CASCADE)
    file = models.CharField(max_length=256)


class Element(models.Model):
    '''This model stores major html elements from a webpage
    currently it will search for div and p tags, see views.py'''
    id = models.AutoField(primary_key=True)
    url = models.ForeignKey(Page, on_delete=models.CASCADE)
    x = models.IntegerField()
    y = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    time_spent = models.IntegerField()