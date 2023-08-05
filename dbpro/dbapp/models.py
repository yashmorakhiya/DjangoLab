from django.db import models

# Create your models here.
class Book(models.Model):
	bname= models.CharField(max_length=30)
	bauthor =models.CharField(max_length=30)
	bdesc=models.TextField(max_length=30)
	bprice=models.IntegerField(default=740)
	def __str__(self):
		return self.bname+" by "+self.bauthor