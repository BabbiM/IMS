from django.http import HttpResponse
from django.shortcuts import  render
from django.contrib import auth
from django.contrib import messages
from .forms import sendIncidentForm
from .forms import assignIncidentForm
#from .forms import SnippetForm
import nltk

def index(request):
    return render(request, 'ImsApp/index.html')

def assign(request):
    if request.method == 'POST':
        form = assignIncidentForm(request.POST)
        if form.is_valid():
            report = form.cleaned_data['report']
            print(report)
    form = assignIncidentForm()
    return render(request, 'ImsApp/assignedincident.html', {'form': form})


def login(request):

        if(request.method=='POST'):
            print('This is statement (mehtod==POST) executed')
            username=request.POST.get('username')
            password=request.POST.get('password')
            print('username: ', username, 'password: ', password)
            user=auth.authenticate(username=username, password=password)
            #request.user.username = username
            print(request.user.username, "Before IFFF")

            #if (username=='Bisrat' and password=='Bisrat') or (username=='Aychew' and password=='aychew') or (username=='Melese' and password=='melese'):
            if user is not None:
                auth.login(request,user)
                print('user is not None exectued')
                print(request.user.username, " Username")

                print(request.user.username, 'xxxxx')
                auth.login(request, user)
                return render(request, 'ImsApp/index.html')
            else:
                print('user not available executed')
                messages.error(request, 'Wrong usrename/password')
        #print('This statement is executed')
        #'maps.html', {'name': username}
        #print ('final try', {'username':request.user.username} )

        return render(request, 'ImsApp/login.html')

def create(request):
    username=login(request)
    return render(request, 'ImsApp/createincident.html')

def closed(request):
    return render (request, 'ImsApp/closedincident.html')

def escalate(request):
    return render (request, 'ImsApp/escalatedincident.html')

def send_incident(request):
    print('send_incdient requested')
    if (request.method == 'GET'):
        print('Method is GET')
        incidentr = request.POST.get('incidentr')
        print(incidentr, 'Incident Report')
        if request.GET.get('reset'):
            print('Reset clicked')
        else:
            print('Reset button not clicked')
    else:
        print('The above IF is not executed')
    return render(request, 'ImsApp/sendincident.html')

def send(request):
    if request.method=='POST':
        form=sendIncidentForm(request.POST)
        if form.is_valid():
            report=form.cleaned_data['report']
            print(report)
        #output= form.initial.get('report')
    form=sendIncidentForm()
    return render(request, 'ImsApp/sendincident.html', {'form': form})


def about(request):
    return render(request, 'ImsApp/about.html')

#def snippet_detail(request):
  #  if request.method=='POST':
 #       form=SnippetForm(request.POST)
 #       if form.is_valid():
 #           print('VALID')
 #   form=SnippetForm()
 #   return render(request, 'sims/sendincident.html', {'form': form})
