from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=4000)
    create_date = models.DateTimeField()
    completed = models.BooleanField(default=0)

    def __unicode__(self):
        return self.title

class UserProperties(models.Model):
    gender = models.CharField(max_length=1)
    height = models.IntegerField()
    weight = models.IntegerField()

#I am not a smart man
class WorkoutType(models.Model):
    name = models.CharField(max_length=100)
    male_rate = models.DecimalField(max_digits=4, decimal_places=2)
    female_rate = models.DecimalField(max_digits=4, decimal_places=2)

class adduser(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=12)
    email = models.EmailField()

    def __unicode__(self):
        return "{0} {1} {2} {3} {4}".format(
            self, self.username, self.password, self.email)

