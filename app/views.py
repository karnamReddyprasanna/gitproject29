from django.shortcuts import render

# Create your views here.
def operations(request):
    d={'a':70,'b':90,'c':100}
    return render(request,'operations.html',d)