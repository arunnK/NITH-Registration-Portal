from django.db import models
from django.contrib.auth.models import User
class registeredclass(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE,null=True)		#user name is rollno of student
	photo=models.ImageField()
	name=models.CharField(max_length=30)
	dob=models.CharField(max_length=15)
	fathername=models.CharField(max_length=30)
	#email=models.EmailField(unique=True)
	#password=models.CharField(max_length=10)
	
	mobile= models.CharField(max_length=30)
	branch=models.CharField(max_length=40)
	address=models.TextField()
	pincode=models.CharField(max_length=30)
	
	def __str__(self):
		return "%s|%s"%(self.name,self.address)

class feeinfo(models.Model):
	year_sem=models.CharField(max_length=10)
	fee=models.IntegerField(default=0)
	def __str__(self):
		return self.year_sem
# Create your models here.

class feedetail(models.Model): 
	user=models.OneToOneField(User, on_delete=models.CASCADE,null=True)
	feeid=models.CharField(max_length=10)	
	year_sem=models.CharField(max_length=10,null=True)
	rollno=models.CharField(max_length=10,unique=True)
	name=models.CharField(max_length=30)
	Amount=models.IntegerField()
	time=models.CharField(max_length=30,null=True)
	flag=models.IntegerField(default=0)
	def __str__(self):
		return self.rollno

class hostel_fee_info(models.Model):
	hostel=models.CharField(max_length=10)
	fee=models.IntegerField(default=0)
	def __str__(self):
		return self.hostel
# Create your models here.

class hostel_fee_detail(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
	hostel=models.CharField(max_length=20,null=True)
	feeid=models.CharField(max_length=10)	
	rollno=models.CharField(max_length=10,unique=True)
	name=models.CharField(max_length=30)
	time=models.CharField(max_length=30,null=True)
	Amount=models.IntegerField()
	def __str__(self):
		return self.rollno
class library_due(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE,null=True)
	rollno=models.CharField(max_length=10,unique=True)
	books=models.IntegerField(default=0)
	due=models.IntegerField(default=0)
	#time=models.CharField(max_length=30,null=True)
	flag=models.IntegerField(default=0)
	def __str__(self):
		return "%s 		|	%d" %(self.rollno,self.due)
class subjects_detail(models.Model):
	semester=models.ForeignKey(feeinfo,on_delete=models.CASCADE)
	branch=models.CharField(max_length=50)
	code=models.CharField(max_length=10)
	subjects=models.TextField()
	lectures=models.IntegerField()
	tutorials=models.IntegerField()
	practicals=models.IntegerField()
	credits=models.IntegerField()
	def __str__(self):
		return "%s    |    %s    |    %s    |    %s    |   " %(self.semester,self.branch,self.code,self.subjects)

class card_detail(models.Model):
	cardno=models.CharField(max_length=16)
	month=models.CharField(max_length=12)
	year=models.CharField(max_length=12)
	cvv=models.CharField(max_length=3)
	def __str__(self):
		return self.cardno