from django.db import models

class BMIRecord(models.Model):
    height = models.FloatField()
    weight = models.FloatField()
    bmi = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'BMI Record ({self.created_at})'
