from django.http.response import JsonResponse
from django.shortcuts import redirect, render



# home.html 연결
def home(request):
    return render(request, 'home.html')

# selectData.html 연결
def selectData(request):
    return render(request, 'selectData.html')