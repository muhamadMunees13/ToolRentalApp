from django.db import models

class login(models.Model):
    name=models.CharField(max_length=40)
    password=models.CharField(max_length=20)
    proof=models.CharField(max_length=30)
    idimg=models.FileField()
    pnum=models.IntegerField()
class products(models.Model):
    pname=models.CharField(max_length=30)
    rent=models.IntegerField()
    detail=models.CharField(max_length=150)
    image=models.FileField()
class prent(models.Model):
    username = models.CharField(max_length=20)
    time = models.DateTimeField()
    product = models.CharField(max_length=20)
    torent = models.IntegerField()
    ndays = models.IntegerField()
    retn = models.DateTimeField()
    orent = models.IntegerField()
class lrent(models.Model):
    prod = models.CharField(max_length=20)
    rentl = models.IntegerField()