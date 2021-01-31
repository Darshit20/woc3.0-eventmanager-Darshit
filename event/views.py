from django.shortcuts import render
from .models import EventReg
from .models import Participant
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
import os
from twilio.rest import Client
from django.contrib import messages
from argon2 import PasswordHasher
from django.core.exceptions import ObjectDoesNotExist
import datetime



# Create your views here.
def home(request):
    return render(request, 'home.html')


def eventReg(request):
    if request.method == "POST":
        event = EventReg()
        event.event_name = request.POST['eName']
        event.event_desc = request.POST['eDesc']
        event.event_loc = request.POST['eLocation']
        event.event_stdate = request.POST['eStdate']
        event.event_endate = request.POST['eEndate']
        event.event_deadline = request.POST['eRegdl']
        event.event_poster = request.FILES['ePoster']
        event.event_host_email = request.POST['hEmail']

        encpwd = PasswordHasher().hash(request.POST['psw'].encode('utf-8'))
        event.event_host_pwd = encpwd
        event.save()



        messages.success(request, 'Your registration is successful kindly check your email for more information.')
        return render(request, 'home.html')
    else:
        return render(request, 'registration.html')


def participantsReg(request):
    eventdata = EventReg.objects.filter(event_deadline__gte=datetime.datetime.now())
    events = {
        "events": eventdata
    }
    if request.method == "POST":
        event = EventReg.objects.get(id=request.POST['event'])

        participants = Participant()
        participants.name = request.POST['pname']
        participants.contact = request.POST['pcontact']
        participants.email = request.POST['pemail']
        participants.reg_event = event.event_name
        participants.reg_type = request.POST['regtype']
        participants.nop = request.POST['tot']

        checkparticipant = Participant.objects.filter(name=participants.name, email=participants.email, reg_event=participants.reg_event)

        if checkparticipant:
            messages.warning(request, 'You have already been registered to this event!!')
            return render(request, 'participants.html', events)
        else:
            participants.save()


        messages.success(request, 'Your registration is successful kindly check your phone for more information. ')
        return render(request, 'home.html')
    else:
        return render(request, 'participants.html', events)


def dashboardLogin(request):
    if request.method == 'POST':

        try:
            usercredential = EventReg.objects.get(id=request.POST['eventid'])
        except ObjectDoesNotExist:
            messages.warning(request, 'Invalid Id')
            return render(request, 'dashboardlogin.html')

        if usercredential.verifylogin(request.POST['psw']):
            participants = Participant.objects.filter(reg_event=usercredential.event_name)
            request.session['user_name'] = usercredential.event_host_email
            if participants:
                messages.success(request, 'Login Successful')
                return render(request, 'dashboardlogin.html',  {"participant": participants})
            else:
                messages.warning(request, 'There are no participants in this event')
                return render(request, 'dashboardlogin.html')
        else:
            messages.warning(request, 'Invalid password!!')
            return render(request, 'dashboardlogin.html')

    return render(request, 'dashboardlogin.html')

def dashboardLogout(request):
    if 'user_name' in request.session:
        messages.success(request, 'You are logged out')
        del request.session['user_name']
        return render(request, 'home.html')
    else:
        return render(request, 'home.html')





