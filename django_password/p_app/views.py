from django.shortcuts import render
from p_app.forms import UserForm,UserProfileInfoForm

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required



# Create your views here.


def index(request):
    return render(request,'p_app/index.html')

def register(request):
    
    registered = False
    
    if request.method == "POST":
       user_form = UserForm(data=request.POST)
       profile_form=UserProfileInfoForm(data=request.POST)
       
       if user_form.is_valid() and profile_form.is_valid():
           
           user = user_form.save()
           user.set_password(user.password)
           user.save()
           
           profile = profile_form.save(commit=False)
           profile.user = user
           
           if 'profile_pic' in request.FILES:
               profile.profile_pic = request.FILES['profile_pic']
           
           profile.save()
            
           registered = True
            
           
       else:
            print(user_form.errors,profile_form.errors)
            
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    
    return render(request,'p_app/registration.html', {'user_form':user_form,'profile_form':profile_form,'registered':registered})



@login_required
def special(request):
    return HttpResponse("You are Loged in, Nice")
@login_required
def user_logout(request):
    logout(request)
    #return HttpResponseRedirect('index')
    return HttpResponseRedirect(reverse('index'))


def user_login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username,password=password)
        
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("someone trid to login and faild")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("invalid login details supplied!")
    else:
        return render(request,'p_app/login.html',{})
        
