from django.db import models

# Create your models here.
class Beer(models.Model):
  name = models.CharField(max_length=200)
  def __unicode__(self):
    return self.name

class Bar(models.Model):
  name = models.CharField(max_length=200)
  def __unicode__(self):
    return self.name
  beers = models.ManyToManyField(Beer)
