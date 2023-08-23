from django.db import models

# Create your models here.
class table1(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name

class table2(models.Model):
    tname = models.CharField(max_length=250)
    timg = models.ImageField(upload_to='pics')
    details = models.TextField()

    def __str__(self):
        return self.tname

