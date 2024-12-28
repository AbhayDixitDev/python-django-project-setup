from django.shortcuts import render,redirect
from django.http import HttpResponse


def home(request):
    return HttpResponse('<style> p:hover { background-color: yellow; } </style><marquee behavior="alternate" style="text-align:center"><p style="background-color:red;color:white;text-align:center;width:100px">hello</p></marquee>')