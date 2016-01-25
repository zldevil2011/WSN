#coding=utf-8
import sys
from app.models import Air, Water
from django.shortcuts import render
from django.http import HttpResponse
import random
import time

def all_screen(request):
    return render(request, "all_screen.html", {})
# Create your views here.

