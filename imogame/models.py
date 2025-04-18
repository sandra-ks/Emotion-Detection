from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Kids(models.Model):
	index=models.CharField(max_length=255, blank=True, null=True)
	name=models.CharField(max_length=255, blank=True, null=True)
	age=models.CharField(max_length=255, blank=True, null=True)
	guardian = models.ForeignKey(User, on_delete=models.CASCADE)
	level = models.CharField(max_length=255, blank=True, null=True)
	training=models.BooleanField(default = False)
	l1=models.BooleanField(default = False)
	l2=models.BooleanField(default = False)
	l3=models.BooleanField(default = False)
	status=models.CharField(max_length=255, blank=True, null=True)
	l1acc = models.CharField(max_length=255, blank=True, null=True)
	l2acc = models.CharField(max_length=255, blank=True, null=True)
	l3acc = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
	    return str(self.name)


class Level1(models.Model):
	index=models.CharField(max_length=255, blank=True, null=True)
	surprise=models.ImageField(default='default.jpg', upload_to='l1_pics')
	fear=models.ImageField(default='default.jpg', upload_to='l1_pics')
	happy = models.ImageField(default='default.jpg', upload_to='l1_pics')
	sad = models.ImageField(default='default.jpg', upload_to='l1_pics')
	neutral = models.ImageField(default='default.jpg', upload_to='l1_pics')
	angry = models.ImageField(default='default.jpg', upload_to='l1_pics')
	disgust = models.ImageField(default='default.jpg', upload_to='l1_pics')

	def __str__(self):
	    return str(self.index)


class Level2(models.Model):
	index=models.CharField(max_length=255, blank=True, null=True)
	surprisevid=models.FileField(default='default.jpg', upload_to='l2_vids')
	fearvid=models.FileField(default='default.jpg', upload_to='l2_vids')
	happyvid = models.FileField(default='default.jpg', upload_to='l2_vids')
	sadvid = models.FileField(default='default.jpg', upload_to='l2_vids')
	neutralvid = models.FileField(default='default.jpg', upload_to='l2_vids')
	angryvid = models.FileField(default='default.jpg', upload_to='l2_vids')
	disgustvid = models.FileField(default='default.jpg', upload_to='l2_vids')

	def __str__(self):
	    return str(self.index)


class Level3(models.Model):
	emot=models.ImageField(default='default.jpg', upload_to='l1_pics')
	name=models.CharField(max_length=255, blank=True, null=True)
	def __str__(self):
	    return str(self.name)


class Counter(models.Model):
	count=models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
	    return str(self.count)