from django.shortcuts import render, get_object_or_404 ,redirect
from django.utils import timezone
from .forms import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TagSerializer
from functools import reduce
from django.db.models import Q
import operator

# Create your views here.

def task_list(request):
    tasks = Task.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    data = {'tasks':tasks}
    return render(request, 'klvr/task_list.html', data)

def task_detail(request,pk):
    task = get_object_or_404(Task, pk=pk)
    print(task.tags.all)
    for tag in task.tags.all():
        print(tag.tagname)
    return render(request,'klvr/task_detail.html',{'task':task})

def task_new(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        # print(form.tagger)
        if form.is_valid():
            post = form.save(commit=False)
            print(post.tagger)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            p = Task.objects.get(author=request.user, title=post.title)
            print("SAVED")
            tags = post.tagger.split(",")
            print(post.id)
            for t in tags:
                if (t != ''):
                    tag = Tag.objects.get(id=t)
                    p.tags.add(tag)

            return redirect('/')
        else:
            print("FAILED")
    else:
        form = TaskForm()
        print("NOT REQUEST")
    return render(request, 'klvr/task_new.html', {'form': form })


def task_edit(request, pk):
    post = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('klvr.views.post_detail', pk=post.pk)
    else:
        form = TaskForm(instance=post)
    return render(request, 'klvr/post_new.html', {'form': form})


class TagList(APIView):

    def get(self,request):
        if(request.GET.get('search') is None):
            tags = Tag.objects.all()
        else:
            search = request.GET.get('search')
            tags = Tag.objects.filter(tagname__contains= search) 
        serializer = TagSerializer(tags,many=True)
        return Response(serializer.data)
 
    def id(self,request,id):
        tags = Tag.objects.filter(id=id)
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

    def set(self):
        print("hi")
        pass;