from django.db import models
from django.contrib.auth.models import User , Tag
from django.utils import timezone



class Task(models.Model):
    author = models.ForeignKey('auth.User',related_name='task_author')
    title = models.CharField(max_length=200)
    text = models.TextField()
    tags = models.ManyToManyField(Tag,blank=True)
    tagger = models.CharField(max_length=1000,default='null',blank=False)
    published_date = models.DateTimeField(default=timezone.now)
    deadline = models.DateField(blank=False, null=True)
    price = models.IntegerField(default=0)
    workers = models.ManyToManyField(User,related_name="task_workers",blank=True)

    def __str__(self):
        return self.title

    def givemetags(self):
        print(self.tags)
        return self.tags

