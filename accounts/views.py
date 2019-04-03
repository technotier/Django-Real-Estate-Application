from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact

# Create your views here.
def register(request):
    if request.method == "POST":
        # Get Form Values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "That username is already taken")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "That Email already taken")
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=password, email=email)
                    # auth.login(request, user)
                    # messages.success(request, "You are now logged in")
                    # return redirect('index')
                    user.save()
                    messages.success(request, "You are now registered.")
                    return redirect('login')
        else:
            messages.error(request, "Password don't match!")
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid User")
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    # logout(request)
    # messages.success(request, "You have been logged out..")
    # return redirect('login')
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "You are logged out")
        return redirect('login')

def dashboard(request):

    user_contact = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context = {
        "user_contact": user_contact
    }

    return render(request, "accounts/dashboard.html", context)
