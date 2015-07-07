from django.db import models

class Module(models.Model):
	name = models.CharField(max_length=30)
	short_description = models.TextField()
	description = models.TextField()
	max_participants = models.IntegerField(null = True)
	current_participants = models.IntegerField()
	registration_deadline = models.DateField()
	number_of_days = models.IntegerField()
	image_file = models.ImageField(upload_to='school/')

	def __str__(self):
		return self.name

class Participant(models.Model):

	f_name = models.CharField(max_length=20)
	l_name = models.CharField(max_length=20)
	email = models.EmailField()
	contact_number = models.CharField(max_length=15, null=True)
	confirmed = models.BooleanField(default = False)
	best_suited_time = models.TimeField(null = True)
	course_registered = models.ForeignKey('school.Module')
	comment = models.TextField(null = True)

	def __str__(self):
		return self.f_name + ' ' + self.l_name