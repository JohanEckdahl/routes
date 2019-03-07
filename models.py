from django.db import models
from django.urls import reverse

class Route(models.Model):

	COLORS = (
		('GREEN', 'Green'),
		('RED', 'Red'),
		('BLUE','Blue'),
		('PURPLE','Purple'),
		('ORANGE', 'Orange'),
		('PINK', 'Pink'),
		('YELLOW', 'Yellow'),
		('BLACK', 'Black'),
		('WHITE', 'White'),
		)

	TAPE = (
		('ORANGE', 'Orange 3a-4c'),
		('GREEN', 'Green 4c-5c'),
		('RED','Red  5c-6b'),
		('BLUE', 'Blue 6a+-6c'),
		('BLACK', 'Black 6c-7a+'),
		('WHITE', 'White 7b-7c'),
		('PINK', 'Pink >7c'),
		)


	GRADES = (
		('3', '3'),
		('4', '4'),
		('5a','5a'),
		('5b','5b'),
		('5c', '5c'),
		('6a', '6a'),
		('6a+', '6a+'),
		('6b', '6b'),
		('6b+', '6b+'),
		('6c','6c'),
		('6c+', '6c+'),
		('7a', '7a'),
		('7a+', '7a+'),
		('7b', '7b'),
		('>7b', '>7b'),
		)
	name = models.CharField(max_length=100, blank=True)
	date_set = models.DateField(blank=False)
	wall = models.PositiveSmallIntegerField(blank=False)
	color = models.CharField(max_length=20, blank=False, choices=COLORS)
	setter = models.CharField(max_length=200, blank=True)
	grade = models.CharField(max_length=5, blank=True, choices=GRADES)
	grade_confirmed = models.BooleanField(default=False)
	coming_down = models.BooleanField(default=False)
	tape = models.CharField(max_length=20, blank=True, choices=TAPE)
	def comment_count(self):
		return len(Comment.objects.filter(route = self))

	#def get_absolute(self):
	#	return reverse('route:index')
	def __str__(self):
		string = ('Wall {}, {}  {}').format(
					str(self.wall),
					str(self.color),
					str(self.name),
					)
		return string
	class Meta:
		get_latest_by = 'wall'


class Boulder(Route):
	def __str__(self):
		return 'boulder'

class Comment(models.Model):

	route= models.ForeignKey(Route, on_delete=models.CASCADE, blank=False)
	username = models.CharField(max_length=50, blank=False)
	date = models.DateTimeField(auto_now_add=True, blank=False)
	body = models.CharField(max_length = 1500, blank=False)
	
	def get_absolute_url(self):
		return reverse('index')

	def __str__(self):
		string = "comment" #("comment {}").format(self.id)
		return string
	
