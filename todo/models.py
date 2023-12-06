from django.db import models

# Create your models here.
class Item(model.Model):
    name = models.Charfield(max_lenght=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)