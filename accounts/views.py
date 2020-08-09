from django.shortcuts import render,redirect
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

# Create your views here.
def signup(request):
    
    if request.method =="POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password2 = request.POST['password2']
        password1 = request.POST['password1']

        if password1 == password2:
            if User.objects.filter(username =username).exists():
                messages.info(request,'Username Taken')
                return redirect('signup')
            
            elif User.objects.filter(email = email).exists():
                messages.info(request,'Email Exists')
                return redirect('signup')
            else:
                # send_mail(
                #     'Welcoming to Green Orchids Resort',
                #     'Congratulations!!, You have successfully registered into Green Orchids. Stay in contact, Enjoy our services. Thanking You , regards Green Orchids Owner ',
                #     settings.EMAIL_HOST_USER,   
                #     [email],    
                #     fail_silently = False   
                # ) 
                user = User.objects.create_user(username = username,first_name = first_name,last_name = last_name,email= email, password = password1)
                user.save()   
                return redirect('login') 
        else:
            messages.info(request,'Wrong Password')  
            return redirect('signup')  
    else:
        return render(request,'signup.html')   

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username ,password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)  # Important!
#             messages.success(request, 'Your password was successfully updated!')
#             return redirect('notes')
#     else:
#         form = PasswordChangeForm(request.user)
#     return render(request, 'change_password.html', {
#         'form': form
#     })    





