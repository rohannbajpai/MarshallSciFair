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
    judge = models.CharField(max_length = 64, default="Judge1")
    def __str__(self):
        return str(self.a_id) + ", " + str(self.judge)
