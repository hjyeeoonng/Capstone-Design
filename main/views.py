from django.shortcuts import render

# Create your views here.
def mainpage(request):
        return render(request, 'main/mainpage.html')

def employee_call(request):
        return render(request, 'main/employee_call.html')