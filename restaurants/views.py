# =#= coding: utf-8 -*-
from django.shortcuts import render_to_response
from django import template
from django.template.loader import get_template

# Create your views here.
def menu(request):
  food1 = {'name':'cake','price':35, 'comment':'good', 'is_spicy':False}
  food2 = { 'name':'蒜泥白肉', 'price':100, 'comment':'人氣推薦', 'is_spicy':True }
  foods = [food1,food2]
  return render_to_response('restaurant/menu.html',locals())
