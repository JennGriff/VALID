from django.db import models
from django.utils.timezone import now

#class Prof(models.Model):
#    title=models.CharField(max_length=100)
#
#    def __str__(self):
#        return self.title

class EmergencyReasons(models.Model):
    title=models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Emergency(models.Model):
    fullName = models.CharField(max_length=100, default = 'First, Last Name')
    CSU_ID = models.CharField(max_length=999999999, default = 000000000)
    #prof = models.ForeignKey(Prof, on_delete=models.CASCADE, default = "Professor Pickle")
    startDate = models.DateField(default = now)
    reason = models.ForeignKey(EmergencyReasons, on_delete=models.CASCADE)
    shortDesc = models.TextField(blank=True)

class ScheduledReasons(models.Model):
    title=models.CharField(max_length=100)  

    def __str__(self):
        return self.title

#class Course(models.Model):
#    title=models.CharField(max_length=100)

#    def __str__(self):
#        return self.title

class Scheduled(models.Model):
    fullName = models.CharField(max_length=100, default = 'First, Last Name')
    CSU_ID = models.CharField(max_length=999999999, default = 000000000)
    startDate = models.DateField(default = now)
    endDate = models.DateField()
    reason = models.ForeignKey(ScheduledReasons, on_delete=models.CASCADE)
    shortDesc = models.TextField(blank=True)
    Verification = models.FileField(upload_to = 'verifyDocs/', default = False, blank = True, null = True)
    #prof = models.ForeignKey(Prof, on_delete=models.CASCADE)