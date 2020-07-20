from django.db import models

# Create your models here.

class First_app(models.Model):
	title = models.CharField(max_length=50,verbose_name='Title')
	completed = models.BooleanField(verbose_name='Status')

	def __str__(self):
		return self.title
