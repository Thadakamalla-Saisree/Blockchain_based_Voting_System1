from django.db import models
# Create your models here.



class users(models.Model):
	uid=models.CharField(max_length=100);
	name=models.CharField(max_length=100);
	email=models.CharField(max_length=100);
	contact=models.CharField(max_length=100);
	address=models.CharField(max_length=100);
	pwd=models.CharField(max_length=100);


class election(models.Model):
	name=models.CharField(max_length=100);
	location=models.CharField(max_length=100);
	stz=models.CharField(max_length=100);
	
class candidates(models.Model):
	eid=models.CharField(max_length=100);
	cname=models.CharField(max_length=100);
	party=models.CharField(max_length=100);
	born=models.CharField(max_length=100);
	education=models.CharField(max_length=100);
	description=models.CharField(max_length=1000);
	photo=models.CharField(max_length=1000);
	symbol=models.CharField(max_length=1000);
	stz=models.CharField(max_length=100);
	
class feedback(models.Model):
	name=models.CharField(max_length=100);
	uid=models.CharField(max_length=100);
	feedback=models.CharField(max_length=1000);

class announcement(models.Model):
	dat_e=models.CharField(max_length=100);
	announcement=models.CharField(max_length=1000);
	stz=models.CharField(max_length=100);

class records(models.Model):
	eid=models.CharField(max_length=100);
	user=models.CharField(max_length=100);


