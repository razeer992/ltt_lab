from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Conveyor(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)   
    mine = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Belt(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    endurance = models.CharField(max_length=200)
    width = models.IntegerField()
    describe = models.TextField()    

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Press(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    series_number = models.CharField(max_length=200)
    manufacture_date = models.CharField(max_length=200)
    width = models.IntegerField()
    manufacturer = models.CharField(max_length=200)
    length = models.IntegerField()
    manual = models.FileField(upload_to='uploads/')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Splice(models.Model):
    owner = models.ForeignKey(User, related_name='created', on_delete=models.CASCADE)
    when_made = models.DateField(auto_now_add=True)
    when_modify = models.DateField(auto_now=True)
    belt_type = models.ForeignKey(Belt, related_name='belts', on_delete=models.CASCADE)
    conveyor_machine = models.ForeignKey(Conveyor, related_name='conveyors', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/')
    angle = models.IntegerField(blank=True, null=True)
    angle_length = models.IntegerField(blank=True, null=True)
    length = models.IntegerField(blank=True, null=True)
    slevel_op = models.IntegerField(blank=True, null=True) 
    slevel_mag = models.IntegerField(blank=True, null=True)
    time = models.IntegerField(blank=True, null=True) 
    temperature = models.IntegerField(blank=True, null=True)
    pressure = models.IntegerField(blank=True, null=True)
    press = models.ForeignKey(Press, related_name='presses', on_delete=models.CASCADE)

    class Meta:
        ordering = ('when_made',)

