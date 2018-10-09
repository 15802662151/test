#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse

# from .forms import AddForm
import forms

def index(request):
    if request.method =="POST":
        form = forms.AddForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a)+int(b)))
    else:
        form = forms.AddForm()
    return render(request,'index.html',{'form':form})
