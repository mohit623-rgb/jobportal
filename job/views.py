from django.shortcuts import render
from .models import *
from random import randint
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact

# Create your views here.
def IndexPage(request):
    return render(request,"app/index.html")
def Joblist(request):
    return render(request,"app/job-list.html")
def About(request):
    return render(request,"app/about.html")
def Category(request):
    return render(request,"app/category.html")
def Testimonial(request):
    return render(request,"app/testimonial.html")
# views.py
from django.shortcuts import render
from django.contrib import messages
from .models import UserAccount




def register_view(request):
    if request.method == "POST":
        role = request.POST.get("role")
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        cpassword = request.POST.get("cpassword")

        # 🔒 Role validation
        if role == "=====Select Role=====":
            messages.error(request, "Please select a role")
            return render(request, "app/register.html")

        # 🔒 Password match
        if password != cpassword:
            messages.error(request, "Passwords do not match")
            return render(request, "app/f404.html")  

        # 🔒 Email already exists
        if UserAccount.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return render(request, "app/f404.html")  

        # ✅ Save data
        UserAccount.objects.create(
            role=role,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password  # ⚠️ plain (see note below)
        )

        messages.success(request, "Account created successfully. Please login.")
        return render(request, "app/f404.html")  # ✅ सही behaviour

    return render(request, "app/register.html")
def signup_view(request):
    if request.method == "POST":
        role = request.POST.get("role")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # 🔒 Role validation
        if role == "=====Select Role=====":
            messages.error(request, "Please select a role")
            return render(request, "app/f404.html")

        # 🔒 Email already exists
        if UserAccount.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return render(request, "app/index.html")

        # ✅ DATA STORE (REGISTER USER)
        UserAccount.objects.create(
            role=role,
            email=email,
            password=password   # ⚠️ plain (see note below)
        )

        messages.success(request, "Account created successfully. Please login.")
        return render(request, "app/index.html")
   # ✅ correct behaviour

    return render(request, "app/f404.html")

def contact_view(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message"),
        )
        return render(request, "app/contact.html",)

    return render(request, "app/contact.html")

def OTPPage(request):
    return render(request,"app/otpverify.html")

def Otpverify(request):
    
    return render(request,"app/f404.html") 
    
def LoginUser(request): #phle ekk function banaya uska name Login rkaha and request pass ki usmein 
   
    return redirect('index')







