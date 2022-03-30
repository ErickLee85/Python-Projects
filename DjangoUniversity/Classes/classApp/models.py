from django.db import models


class Classes(models.Model):
    Title = models.CharField(max_length=50, default="", blank=True, null=False)
    Course_Number = models.IntegerField(max_length=20, default="", blank=True, null=False)
    Instructor_Name = models.CharField(max_length=50, default="", blank=True, null=False)
    Duration = models.FloatField(default=0.00)

    objects = models.Manager()

    def __str__(self):
        return self.Title


