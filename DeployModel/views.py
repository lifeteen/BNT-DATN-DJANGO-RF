from typing import List
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
import pandas as pd
import joblib

def home(request):
    return render(request,"home.html")

def resulst(request):
    cls=joblib.load('finalized_model.sav')
    lis=[]
    lis.append(request.GET['mh'])
    lis.append(request.GET['mt'])
    lis.append(request.GET['cl'])
    lis.append(request.GET['bt'])
    lis.append(request.GET['cl1'])
    lis.append(request.GET['cd'])
    lis.append(request.GET['ct'])
    lis.append(request.GET['st'])
    lis.append(request.GET['pq'])
    lis.append(request.GET['rg'])
    lis.append(request.GET['bl'])
    lis.append(request.GET['cm'])

    ans=cls.predict([lis])

    return render(request,"result.html",{'something':True,'ans':ans,'lis':lis})