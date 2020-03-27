from django.db import models
import time

# Create your models here.

class Examiner(models.Model):
	name = models.CharField(max_length=100, default="Anonymous")
	info = models.TextField(default="No information available")

class QuizCatalog(models.Model):
	examiner = models.ForeignKey(Examiner, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	programme = models.CharField(max_length=255, default="general")
	course = models.CharField(max_length=255, default="general paper")
	level = models.IntegerField(default=100)
	image = models.CharField(max_length=50)
	allocated_time = models.IntegerField(default=10)
	rating = models.CharField(max_length=50, default="normal")
	date = models.CharField(max_length=25, default=time.asctime())


class Question(models.Model):
	quiz_catalog = models.ForeignKey(QuizCatalog, on_delete=models.CASCADE)
	question = models.TextField()
	answer = models.TextField()


class Choice(models.Model):
	answer = models.ForeignKey(Question,on_delete = models.CASCADE)
	choice = models.TextField()

class Tutorials(models.Model):
	form = models.CharField(max_length=15)


	