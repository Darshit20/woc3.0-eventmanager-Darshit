from django.db import models

# Create your models here.
class EventReg(models.Model):
    event_name = models.CharField(max_length=255)
    event_desc = models.CharField(max_length=255)
    event_loc = models.CharField(max_length=100)
    event_stdate = models.DateTimeField()
    event_endate = models.DateTimeField()
    event_deadline = models.DateTimeField()
    event_poster = models.ImageField(upload_to="eventPoster/")
    event_host_email = models.EmailField()
    event_host_pwd = models.CharField(max_length=50)

    def __str__(self):
        return self.event_name


class Participant(models.Model):
    name = models.CharField(max_length=255)
    contact = models.PositiveIntegerField()
    email = models.EmailField()
    reg_event = models.CharField(max_length=255)
    reg_type = models.CharField(max_length=255)
    nop = models.PositiveIntegerField()

    def __str__(self):
        return self.name












