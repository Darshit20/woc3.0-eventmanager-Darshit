from django.shortcuts import render
from .models import EventReg
from .models import Participant
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
import os
from twilio.rest import Client
from django.contrib import messages

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
        event.event_host_pwd = request.POST['psw']
        event.save()

        subject = 'Event Registration '
        message = 'Thank you for registering your event with us.' \
                  f'\n\nEvent Name : {event.event_name}' \
                  f'\nEvent Id : {event.id}' \
                  '\n\nYou can now review the participants of your event through our portal.' \
                  '\n\n\n\n\n\n\nTeam GameOn'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['nawog85659@aiclbd.com', ]

        send_mail(subject, message, email_from, recipient_list)
    return render(request, 'registration.html')


def participantsReg(request):
    eventdata = EventReg.objects.filter(event_deadline__gte=datetime.datetime.now())
    events = {
        "events": eventdata,
        "error": 'You have already registered to this event'
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

        checkparticipant = Participant.objects.filter(name=participants.name, email=participants.email,reg_event=participants.reg_event)

        if checkparticipant:
            return render(request, 'participants.html', events)


        client = Client()
        message = client.messages \
            .create(
            body="""\nThank you"""+participants.name+""" for registering your participation with us.
                    
            Participation ID:"""+str(participants.id)+"""
            Event Name : """+event.event_name+"""
            Location : """+event.event_loc+"""
            Time : """+str(event.event_stdate)+"""-"""+str(event.event_endate)+""""
            No. of people : """+str(participants.nop)+"""
                    
            -GameOn""",
            from_='+15185030699',
            to='+91'+str(participants.contact)
        )
        participants.save()


    return render(request, 'participants.html', {'events': event2})


def dashboardLogin(request):
    return render(request, 'dashboardlogin.html')
