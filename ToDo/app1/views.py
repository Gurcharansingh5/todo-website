from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.
# register page
def index(request):
    if request.method == 'POST':
        usernames = request.POST['usernames']
        passwords = request.POST['passwords']
        print(usernames,passwords)
        user = User.objects.create_user(username=usernames,password=passwords)
        # login(request,user)
        # return redirect('index')
        return HttpResponse("registered successfuully")
    else:
        return render(request,'index.html')
# login page
def authlogin(request):
    if request.method == 'POST':
        usernames = request.POST['usernames']
        passwords = request.POST['passwords']
        print(usernames,passwords)
        user = authenticate(request, username=usernames, password=passwords)
        if user is not None:
            login(request,user)
            return render(request,'login.html')
            # return redirect('authenticate')
    else:
        return render(request,'login.html')
def logoutuser(request):
    logout(request)
    return  redirect('authlogin')
# def updateuser(request):
#     if request.method == 'POST':
#         usernames = request.POST['usernames']
#         # passwords = request.POST['passwords']
#         user = User(username=usernames)
#         user.save()
#         return HttpResponse('username update successulluy')
#     else:
#         return render(request,'update.html')
