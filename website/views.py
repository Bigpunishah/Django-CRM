from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from.models import Record

# Create a dir named `templates` to add .html files
# Create your views here.
def home(request):
    records = Record.objects.all()

    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username'] # These are the html field names on the home.html file
        password = request.POST['password']

        #Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in")
            return redirect('home')
        else:
            messages.error(request, "There was an error try again.")
            return redirect('home')

    # If not logging in then else send home
    else:
        return render(request, 'home.html', {'records': records})




# These functions cannot be names login/logout: conflict with imports
def login_user(request):
    # Save this function for a seperate screen if wanted
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')

def register_user(request):
    # Check to see if it is the post metod
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate & login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered!")
            return redirect('home')
        # Pick up at 1:15:00
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})

# Showing the individual record
def customer_record(request, primary_key):
    if request.user.is_authenticated:
        # Look up record
        customer_record = Record.objects.get(id = primary_key)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request, "Must be logged in!")
        return redirect('home')