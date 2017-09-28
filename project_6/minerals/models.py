#the homepage will be a list of all the minerals in the database.
#clicking on a minerals name opens a page that displays information about the 
#mineral. 
#download the html/css pages. Do not alter the 'global.css' page. 
#So you are making only 2 pages. A 'list' page (home page), and a 'detail' page. 





from django.db import models

# Create your models here.
class Mineral(models.Model):
	"""the model for all of the minerals and their details"""
	image_filename = models.TextField(blank=True, default='')
	formula = models.TextField(blank=True, default='')
	optical_properties = models.TextField(blank=True, default='')
	cleavage = models.TextField(blank=True, default='')
	image_caption = models.TextField(blank=True, default='')
	streak = models.TextField(blank=True, default='')
	name = models.TextField(blank=True, default='')
	crystal_system = models.TextField(blank=True, default='')
	group = models.TextField(blank=True, default='')
	specific_gravity = models.TextField(blank=True, default='')
	strunz_classification = models.TextField(blank=True, default='')
	crystal_symmetry = models.TextField(blank=True, default='')
	mohs_scale_hardness = models.TextField(blank=True, default='')
	unit_cell = models.TextField(blank=True, default='')
	refractive_index = models.TextField(blank=True, default='')
	category = models.TextField(blank=True, default='')
	luster = models.TextField(blank=True, default='')
	color = models.TextField(blank=True, default='')
	crystal_habit = models.TextField(blank=True, default='')
	diaphaneity = models.TextField(blank=True, default='')
	













