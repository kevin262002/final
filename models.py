from django.db import models


class Member(models.Model):
  firstname = models.CharField(max_length=25)
  lastname = models.CharField(max_length=25)
  roll_no = models.IntegerField()
  city = models.CharField(max_length=20)




    