from django.shortcuts import render,HttpResponse 

# Create your views here.
def inicio(request):
    return render(request,"index.html")

def segunda(request):
    return render(request,"principal.html")