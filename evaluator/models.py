from django.db import models

# Create your models here.
class projects(models.Model):
    a_id = models.IntegerField()
    p_type = models.CharField(max_length=64, null = True, blank = True)
    research_question = models.IntegerField(default=0)
    dam = models.IntegerField(default=0)
    execution = models.IntegerField(default=0)
    creativity = models.IntegerField(default=0)
    presentation = models.IntegerField(default=0)
    judge = models.CharField(max_length = 64, default="")
    def __str__(self):
        return str(self.judge) + ", " +  str(self.a_id)

class event(models.Model):
    time_from = models.CharField(max_length=5, default = "")
    time_to = models.CharField(max_length =5, default = "")
    project =  models.ForeignKey(projects, on_delete=models.CASCADE, related_name ="project", blank = True, null = True)
    def __str__(self):
        return "Project id: " + str(self.project.a_id) + ", Judge: " + str(self.project.judge) 

class schedule(models.Model):
    judge = models.CharField(max_length = 64, default="")
    event1 = models.ForeignKey(event, on_delete=models.CASCADE, related_name ="event1")
    event2 = models.ForeignKey(event, on_delete=models.CASCADE, related_name ="event2")
    event3 = models.ForeignKey(event,on_delete=models.CASCADE, related_name ="event3")
    event4 = models.ForeignKey(event,on_delete=models.CASCADE ,related_name ="event4")
    event5 = models.ForeignKey(event, on_delete=models.CASCADE, related_name ="event5")
    event6 = models.ForeignKey(event,on_delete=models.CASCADE, related_name ="event6")
    event7 = models.ForeignKey(event,on_delete=models.CASCADE, related_name ="event7")
    event8 = models.ForeignKey(event, on_delete=models.CASCADE, related_name ="event8")
    event9 = models.ForeignKey(event, on_delete=models.CASCADE, related_name ="event9")
    def __str__(self):
        return "Schedule for: " + self.judge


