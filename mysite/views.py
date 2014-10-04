# =#= coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django import template
from django.template.loader import get_template

def welcome(request):
  if 'user_name' in request.GET:
    return HttpResponse('Welcome'+request.GET['user_name'])
  else:
    return render_to_response('test/welcome.html',locals())

def menu(request):
  food1 = {'name':'cake','price':35, 'comment':'good', 'is_spicy':False}
  food2 = { 'name':'蒜泥白肉', 'price':100, 'comment':'人氣推薦', 'is_spicy':True }
  foods = [food1,food2]
  return render_to_response('test/menu.html',locals())

def here(request):
  return HttpResponse('Hey, I am here! 在此')

def math(request,a,b):
  aa = int(a) + int(b)
  bb = int(a) - int(b)
  return render_to_response('test/math.html',locals())
