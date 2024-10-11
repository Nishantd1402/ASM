from django.shortcuts import render, redirect
from django.contrib.auth import authenticate , login 
from django.contrib import messages
from .models import DeptHead, Student, Department
import pandas as pd
from django.http import HttpResponse
import openpyxl

def index(request):
    departments = Department.objects.all()
    context = {
        'departments': departments,
    }
    return render(request, 'myapp/index.html' , context)

def event1(request):
    request.session['event'] = 'Football'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            # Fetch user by username
            user = DeptHead.objects.get(username=username)
            
            
            # Check if the password matches (assuming password is hashed)
            if user.check_password(password):
                # Authentication successful, redirect to registration
                return redirect('register')
            else:
                # Password doesn't match, show an error message
                messages.error(request, "Invalid password, please try again.")
        
        except DeptHead.DoesNotExist:
            # Username doesn't exist, show an error message
            messages.error(request, "Invalid username, please try again.")
    
    # Render the event1 page with the login form
    return render(request , 'myapp/event1_login.html')
    

def event2(request):
    request.session['event'] = 'Cricket'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            # Fetch user by username
            user = DeptHead.objects.get(username=username)
            
            # Check if the password matches (assuming password is hashed)
            if user.check_password(password):
                # Authentication successful, redirect to registration
                return redirect('register')
            else:
                # Password doesn't match, show an error message
                messages.error(request, "Invalid password, please try again.")
        
        except DeptHead.DoesNotExist:
            # Username doesn't exist, show an error message
            messages.error(request, "Invalid username, please try again.")
    
    # Render the event1 page with the login form
    return render(request, 'myapp/event2_login.html')

def event3(request):
    request.session['event'] = 'Basketball'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            # Fetch user by username
            user = DeptHead.objects.get(username=username)
            
            # Check if the password matches (assuming password is hashed)
            if user.check_password(password):
                # Authentication successful, redirect to registration
                return redirect('register')
            else:
                # Password doesn't match, show an error message
                messages.error(request, "Invalid password, please try again.")
        
        except DeptHead.DoesNotExist:
            # Username doesn't exist, show an error message
            messages.error(request, "Invalid username, please try again.")
    
    # Render the event1 page with the login form
    return render(request, 'myapp/event3_login.html')

def event4(request):
    request.session['event'] = 'Chess'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            # Fetch user by username
            user = DeptHead.objects.get(username=username)
            
            # Check if the password matches (assuming password is hashed)
            if user.check_password(password):
                # Authentication successful, redirect to registration
                return redirect('register')
            else:
                # Password doesn't match, show an error message
                messages.error(request, "Invalid password, please try again.")
        
        except DeptHead.DoesNotExist:
            # Username doesn't exist, show an error message
            messages.error(request, "Invalid username, please try again.")
    
    # Render the event1 page with the login form
    return render(request, 'myapp/event4_login.html')

def event5(request):
    request.session['event'] = 'Athletics'
    if request.method == 'POST':
                return redirect('register')

    
    # Render the event1 page with the login form
    return render(request, 'myapp/event5_login.html')


def event6(request):
    request.session['event'] = 'Tug of War'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            # Fetch user by username
            user = DeptHead.objects.get(username=username)
            
            # Check if the password matches (assuming password is hashed)
            if user.check_password(password):
                # Authentication successful, redirect to registration
                return redirect('register')
            else:
                # Password doesn't match, show an error message
                messages.error(request, "Invalid password, please try again.")
        
        except DeptHead.DoesNotExist:
            # Username doesn't exist, show an error message
            messages.error(request, "Invalid username, please try again.")
    
    # Render the event1 page with the login form
    return render(request, 'myapp/event6_login.html')

def event7(request):
    request.session['event'] = 'Volleyball'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            # Fetch user by username
            user = DeptHead.objects.get(username=username)
            
            # Check if the password matches (assuming password is hashed)
            if user.check_password(password):
                # Authentication successful, redirect to registration
                return redirect('register')
            else:
                # Password doesn't match, show an error message
                messages.error(request, "Invalid password, please try again.")
        
        except DeptHead.DoesNotExist:
            # Username doesn't exist, show an error message
            messages.error(request, "Invalid username, please try again.")
    
    # Render the event1 page with the login form
    return render(request, 'myapp/event7_login.html')

def event8(request):
    request.session['event'] = 'Handball'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            # Fetch user by username
            user = DeptHead.objects.get(username=username)
            
            # Check if the password matches (assuming password is hashed)
            if user.check_password(password):
                # Authentication successful, redirect to registration
                return redirect('register')
            else:
                # Password doesn't match, show an error message
                messages.error(request, "Invalid password, please try again.")
        
        except DeptHead.DoesNotExist:
            # Username doesn't exist, show an error message
            messages.error(request, "Invalid username, please try again.")
    
    # Render the event1 page with the login form
    return render(request, 'myapp/event8_login.html')

def event9(request):
    request.session['event'] = 'Kabaddi'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            # Fetch user by username
            user = DeptHead.objects.get(username=username)
            
            # Check if the password matches (assuming password is hashed)
            if user.check_password(password):
                # Authentication successful, redirect to registration
                return redirect('register')
            else:
                # Password doesn't match, show an error message
                messages.error(request, "Invalid password, please try again.")
        
        except DeptHead.DoesNotExist:
            # Username doesn't exist, show an error message
            messages.error(request, "Invalid username, please try again.")
    
    # Render the event1 page with the login form
    return render(request, 'myapp/event9_login.html')

def event10(request):
    request.session['event'] = 'Badminton'
    if request.method == 'POST':
                return redirect('register')

    
    # Render the event1 page with the login form
    return render(request, 'myapp/event10_login.html')

def event11(request):
    request.session['event'] = 'Table-Tennis'
    if request.method == 'POST':
                return redirect('register')

    
    # Render the event1 page with the login form
    return render(request, 'myapp/event11_login.html')

def event12(request):
    request.session['event'] = 'Carrom'
    if request.method == 'POST':
                return redirect('register')

    
    # Render the event1 page with the login form
    return render(request, 'myapp/event12_login.html')



def event13(request):
    request.session['event'] = 'Kho-Kho'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            # Fetch user by username
            user = DeptHead.objects.get(username=username)
            
            # Check if the password matches (assuming password is hashed)
            if user.check_password(password):
                # Authentication successful, redirect to registration
                return redirect('register')
            else:
                # Password doesn't match, show an error message
                messages.error(request, "Invalid password, please try again.")
        
        except DeptHead.DoesNotExist:
            # Username doesn't exist, show an error message
            messages.error(request, "Invalid username, please try again.")
    
    # Render the event1 page with the login form
    return render(request, 'myapp/event13_login.html')

def view_draws(request):
    # Logic for handling the view, if needed
    return render(request, 'myapp/Indexdraws.html')

def register(request):
    return render(request, 'myapp/register.html')

def success(request):
    return render(request, 'myapp/success.html')
 
def student_register(request):
    value = request.session.get('event')
    departments = Department.objects.all()
    print(departments)
    print(value)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        prn = request.POST.get('prn')
        email = request.POST.get('email')
        year = request.POST.get('year')
        department_name = request.POST.get('department')
        roll_number = request.POST.get('roll_number')
        mobile_number = request.POST.get('mobile_number')

        # Print POST data for debugging
        print("POST data received:", request.POST)
        

        # Validate that all fields are filled
        if all([first_name, last_name, prn, email, year, department_name, roll_number, mobile_number]):
                try:

                    department = Department.objects.get(dept_name=department_name)
                    # Create and save a new Student object
                    student = Student(
                        first_name=first_name,
                        middle_name=middle_name,
                        last_name=last_name,
                        prn=prn,
                        email=email,
                        event= request.session.get('event'),
                        year=year,
                        department=department,
                        roll_number=roll_number,
                        mobile_number=mobile_number
                    )
                    student.save()
                    print("Student saved successfully!")  # Debugging print statement

                    # Redirect to success page after saving
                    messages.error(request , "succesfully added")
                    return redirect('register')
                except Exception as e:
                    # Print error during saving
                    print(f"Error saving student: {e}")
                    messages.error(request, "An error occurred while saving. Please try again.")
        else:
            messages.error(request, "Please fill in all required fields.")

    context = {
        'event': value,
        'departments': departments
    }

    return render(request, 'myapp/register.html' , context)