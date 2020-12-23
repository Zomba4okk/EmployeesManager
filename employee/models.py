from django.db import models

from computer.models import Computer


class Department(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    floor = models.IntegerField()
    number = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.number)


class Employee(models.Model):
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=False)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, related_name='employees')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')
    computer = models.OneToOneField(Computer, on_delete=models.SET_NULL, null=True, blank=True, related_name='owner')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
