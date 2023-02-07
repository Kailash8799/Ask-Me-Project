from django.shortcuts import render

# Create your views here.

def showallque(request):
    return render(request,'user_que/all_que.html')