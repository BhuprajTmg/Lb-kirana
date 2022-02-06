from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.contrib.auth import  authenticate
from django.contrib.auth.models import auth, User
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render(request, 'index.html')

def homepage(request):
    return render(request, 'homepage.html')

def register(request):
    if request.method =='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(
                            username=username,
                            email=email,
                            password=password)
        user.save()
        print("here")
        return redirect('/login') 

    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('/login')
    else:  
        return render(request, 'login.html') 




def contact(request):
    if request.method == "POST":
        message_name = request.POST['message_name']
        message_email = request.POST['message_email'] 
        message =request.POST['message']

        send_mail(
            message_name, #subject
            message, #message
            message_email, #from email
            # settings.EMAIL_HOST_USER,
            #           ['riyastha406@mail.com'],
            ['bhupraj875@gmail.comm' ], #To email
            # fail_silently= True,
        )   
        return render(request, 'pages/contact.html', {'message_name': message_name}) 

    else:
        return render(request, 'pages/contact.html' , {})
# Auth.login is a default login function given by django.  which checks the data from database and the users given input