from django.http import HttpResponse, JsonResponse
import pandas as pd
from django.shortcuts import render
from django.views import View


def home(request):
    return render(request, 'home.html')


def PandasFunc(request) :
    card_data = pd.read_csv('C:/min/13weeks_MiniProject(2)/card_project_django/card_project/train.csv')
    car_df = card_data.groupby('car')['credit'].mean()
    labels = ['N', 'Y']
    data = []
    for i in car_df:
        data.append(i)
    return JsonResponse(data = {
        'labels':labels,
        'data':data,
    })