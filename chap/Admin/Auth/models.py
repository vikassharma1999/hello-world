from django.db import models

# Create your models here.
class Uploaddb(models.Model):
	title=models.CharField(max_length=20)
	file=models.FileField(blank=True)
	def __str__(self):
		return self.title

