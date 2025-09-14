from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    
    return render(request,'index.html')
    
def about(request):
    return HttpResponse('about page')
def me(request):
    return HttpResponse('me page')
def contect(request):
    return HttpResponse("contect page")
def newuser(request):
    return HttpResponse("newuser page") 

