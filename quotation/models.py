from django.db import models

# Create your models here.


class Quotation(models.Model):
    person = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.content
