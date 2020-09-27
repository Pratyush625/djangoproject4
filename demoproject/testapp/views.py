from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'testapp/index.html')
def courses_view(request):
    return render(request,'testapp/courses.html')
def newbatches_view(request):
    return render(request,'testapp/newbatches.html')
def aboutus_view(request):
    return render(request,'testapp/aboutus.html')
def contactus_view(request):
    return render(request,'testapp/contactus.html')
