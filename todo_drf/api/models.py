from django.db import models

# Create your models here.
class ParkingSpace(models.Model):
  latitude = models.DecimalField(max_digits=9,decimal_places=6)
  longitude = models.DecimalField(max_digits=9,decimal_places=6)
  spaceRow = models.CharField(max_length=2,null=True)
  spaceCol = models.IntegerField(null=True)
  timeOccupied = models.DateTimeField(auto_now=True)
  filled = models.BooleanField(default=False)
  reserved = models.BooleanField(default=False)
  cost = models.DecimalField(default=0,max_digits=8,decimal_places=2)

  def __str__(self):
    return self.serialNo



# Model - parking space
# fields - longitude,latitude,serial no.,time occupied,filled,reserved, cost,user
# Serialised user
# fields - times visited,time saved, user,car model,number plate
