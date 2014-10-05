# =#= coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django import template
from django.template.loader import get_template
from django.contrib import auth
from django.template import RequestContext

def index(request):
  return render_to_response('test/index.html', locals(), context_instance=RequestContext(request))

def logout(request):
  auth.logout(request)
  return HttpResponseRedirect('/index/')

def login(request):
  if request.user.is_authenticated():
    return HttpResponseRedirect('/index/')
  username = request.POST.get('username','')
  password = request.POST.get('password','')
  user = auth.authenticate(username=username, password=password)
  if user is not None and user.is_active:
    auth.login(request,user)
    return HttpResponseRedirect('/index/')
  else:
    return render_to_response('test/login.html','',context_instance=RequestContext(request))

def session_test(request):
  sid = rquest.COOKIES['sessionid']
  s = Session.objects.get(pk=sid)
  s_ifo = 'Session ID:' + sid + '</br>Expire_date:' + str(s.expire_date) + '</br>Data:' + str(s.get_decode())
  return HttpResponse(s_info)

def use_session(request):
  request.session['lucky_number'] = 8
  if 'luck_number' in request.session:
    request.session['lucky_number']
    response = HttpResponse('Your lucky_number is '+lucky_number)
  del request.session['lucky_number']
  return response

def set_c(request):
  response = HttpResponse('Set you lucky_number as 8')
  response.set_cookie('lucky_number',8)
  return response

def get_c(request):
  if 'lucky_number' in request.COOKIES:
    return HttpResponse('Your lucky_number is {0}'.format(request.COOKIES['lucky_number']))
  else:
    return HttpResponse('No Cookies.')

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
