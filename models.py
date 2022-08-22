from datetime import date
from django.db import models

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)
    biocontent = models.CharField(max_length=100)
    emailaddress = models.CharField(max_length=30)
    lastseen = models.TimeField(auto_now=True)
    currentstatus = models.BooleanField(default=True)


class Notifications(models.Model):
    userid = models.ForeignKey(User)
    notificationcontnet = models.CharField(max_length=500)
    notificationtype = models.CharField(max_length=10)
    date = models.DateField(auto_now=True)
    currentstatus = models.BooleanField(default=True)

class Group(models.Model):
    name = models.CharField(max_length=100)


class MultiUser:
    groupid = models.OneToOneField(Group)
    users = models.ManyToManyField(User)


class Message(models.Model) :
    messagecontent = models.CharField(max_length=500)
    sentby = models.CharField(max_length=100)

class Groupchatting (models.Model):
    groupid = models.OneToOneField(Group)
    messageid = models.ManyToManyField(Message)
    seenby = models.IntegerField(max_length=100)
    deliveredto = models.IntegerField (max_length=100)

class OneToOne(models.Model):
    messageid = models.ManyToManyField(Message)    