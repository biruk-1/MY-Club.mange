from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event, Report
from .forms import CreateUserForm, EventForm


def home(request):
    # Logic for the home view
    return render(request, 'club/home.html')




def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully.')
            return redirect('home')  # Replace 'home' with your desired URL name
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'club/login.html')  # Replace 'login.html' with your login template name





def logout_view(request):
    # Logic for the logout view
    logout(request)
    return redirect('club:home')


# @login_required
def member_add(request):
    # Logic for the member add view
    if request.method == 'POST':
        # Process form submission
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            # Additional logic to create a Member object and associate it with the user
            
            messages.success(request, 'Member added successfully.')
            return redirect('home')
        else:
            messages.error(request, 'Error adding member. Please check the form.')
    else:
        form = CreateUserForm()
    
    return render(request, 'club/member_add.html', {'form': form})


@login_required
def member_delete(request, member_id):
    # Logic for the member delete view
    try:
        member = Member.objects.get(id=member_id)
        user = member.user
        user.delete()
        messages.success(request, 'Member deleted successfully.')
    except Member.DoesNotExist:
        messages.error(request, 'Member not found.')
    return redirect('club:member_list')


# @login_required
def event_list(request):
    # Logic for the event list view
    Events = Event.objects.all()
    return render(request, 'club/event_list.html', {'events': Events})


@login_required
def event_add(request):
    
    if request.method == 'POST':
        
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save()
            messages.success(request, 'Event added successfully.')
            return redirect('event_list')
        else:
            messages.error(request, 'Error adding event. Please check the form.')
    else:
        form = EventForm()
    
    return render(request, 'club/event_add.html', {'form': form})


@login_required
def event_detail(request, event_id):
    # Logic for the event detail view
    try:
        event = Event.objects.get(id=event_id)
        return render(request, 'club/event_detail.html', {'event': event})
    except Event.DoesNotExist:
        messages.error(request, 'Event not found.')
        return redirect('club:event_list')


@login_required
def event_delete(request, event_id):
    # Logic for the event delete view
    try:
        event = Event.objects.get(id=event_id)
        event.delete()
        messages.success(request, 'Event deleted successfully.')
    except Event.DoesNotExist:
        messages.error(request, 'Event not found.')
    return redirect('club:event_list')


# @login_required
def generate_report(request):
    # Logic for the report generation view
    # Generate the report
    # Return the report to the user
    return render(request, 'club/generate_report.html')


@login_required
def member_dashboard(request):
    # Logic for the member dashboard view
    # Retrieve relevant data for the member dashboard
    return render(request, 'club/member_dashboard.html')


@login_required
def member_profile(request):
    # Logic for the member profile view
    # Retrieve and display the member's profile information
    return render(request, 'club/member_profile.html')