# =#= coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django import template
from django.template.loader import get_template
from restaurants.models import *
import datetime
from restaurants.forms import *
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

# Create your views here.
def comment(request,id):
    if id:
        r = Restaurant.objects.get(id=id)
    else:
        return HttpResponseRedirect("/rest_list/")
    if 'ok' in request.POST:
      f = CommentForm(request.POST)
      if f.is_valid():
        user = f.cleanded_data['user']#request.POST['user']
        content = f.cleaned_data['content']#request.POST['content']
        email = f.cleaned_data['email']#request.POST['email']
        date_time = datetime.datetime.now()     # 擷取現在時間
        c = Comment(user=user, email=email, content=content, date_time=date_time, restaurant=r)
        c.save()
        f = CommentForm(initial={'user':'it is required'})
      else:
        f = CommentForm(initial={'user':'please'})
        #Comment.objects.create(user=user, email=email, content=content, date_time=date_time, restaurant=r)
    #f = CommentForm()
    return render_to_response('restaurant/comment.html',locals(), context_instance=RequestContext(request))

@login_required
def rest_list(request):
  restaurants = Restaurant.objects.all()
  return render_to_response('restaurant/rest_list.html',locals())

def menu1(request):
  if 'id' in request.GET:
    print(type(request.GET['id']))
    r = Restaurant.objects.get(id=request.GET['id'])
    return render_to_response('restaurant/menu1.html',locals())
  else:
    return HttpResponseRedirect("/rest_list")
    #  return render_to_response('restaurant/menu1.html',locals())
    #else:
    #  return HttpResponseRedirect("/rest_list")

def menu(request):
  path = request.path
  rest = Restaurant.objects.all()
  values = request.META.items()
  values.sort()
  return render_to_response('restaurant/menu.html',locals())
