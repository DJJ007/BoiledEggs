from django.db import models
from django.utils import timezone

# Create your models here.
class Publication(models.Model):
	name = models.CharField("Name of the publiation", max_length = 100)

	def __str__(self):
		return self.name

class Book(models.Model):
	title = models.CharField("Title of the Book", max_length = 100)
	summary = models.TextField("Summary of the book")
	publication = models.ForeignKey(Publication, on_delete = models.CASCADE)
	price = models.IntegerField(default = 100)
	ISBN = models.IntegerField("Enter the ISBN Number")
	published_date = models.DateTimeField()
	
	def __str__(self):
		return self.title

class Author(models.Model): #Use Later
	name = models.CharField("Name of Author", max_length = 100)

	def __str__(self):
		return self.name