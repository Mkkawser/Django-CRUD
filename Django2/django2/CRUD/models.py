from django.db import models


class crudDB(models.Model):
    namedb = models.CharField(max_length=50)
    emaildb = models.CharField(max_length=50)
    phonedb = models.CharField(max_length=50)
