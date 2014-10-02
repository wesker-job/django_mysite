# =#= coding: utf-8 -*-
from django.shortcuts import render_to_response
from django import template
from django.template.loader import get_template
from restaurants.models import *

# Create your views here.
def menu(request):
  rest = Restaurant.objects.all()
  return render_to_response('restaurant/menu.html',locals())
