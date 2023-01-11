from django.shortcuts import render
from .forms import RegistrationForm
from django.http import HttpResponseRedirect
# # Create your views here.
def index(request):
    return render(request,'pages/home.html')
    # response = HttpResponse()
    # response.writelines("<h1>Xin Chào</h1>")
    # response.write("Đây là trang chủ")
    # return response 
def register(request):
    form = RegistrationForm()
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return (HttpResponseRedirect("/"))
    return render(request,'pages/register.html',{'forms':form})
def contact(request):
    return render(request,'pages/contact.html')
def login(request):
    return render(request,'pages/login.html')