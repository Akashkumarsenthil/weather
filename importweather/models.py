from django.db import models

# Create your models here.

from django.db import models

class weatherdata(models.Model):
	city_name 	= models.CharField(max_length = 80)
	city_id 	= models.IntegerField(default=0)
	latitude 	= models.FloatField(null=True , blank=True)
	longitude 	= models.FloatField(null=True , blank=True)
	dt_txt 		= models.DateTimeField()
	temp 		= models.FloatField(null = False)
	temp_min 	= models.FloatField(null = False)
	temp_max 	= models.FloatField(null = False)
	pressure 	= models.FloatField(null = False) 
	sea_level 	= models.FloatField(null = False)
	grnd_level 	= models.FloatField(null = False)
	humidity 	= models.FloatField(null = False)
	main 		= models.CharField(max_length=200)
	description = models.CharField(max_length=30)
	clouds 		= models.IntegerField(null=False)
	wind_speed 	= models.FloatField(null = False)
	wind_degree = models.FloatField(null = False)


	def __str__(self):
		return self.city_name