from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Template,Context
from django.template.loader import get_template
from django.core.exceptions import ObjectDoesNotExist
#import pymysql as MySQLdb
#from django.shortcuts import render_to_response
from django.template import RequestContext
from register.models import *
from django.core.urlresolvers import reverse

#these are import to get default 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required   #login_required used to limiting access to login user

#User models store the username,password or emailid
from django.contrib.auth.models import User
from .printing import MyPrint
from io import  BytesIO
from django.contrib.admin.views.decorators import staff_member_required
from django.db import IntegrityError
from datetime import date
# Create your views here.
login_error=""
register_error=""
pay_error=""
def index(request):
	if not request.user.is_authenticated():
		return render_to_response("index.html",context_instance=RequestContext(request))
	else:
		username=request.user.username
		if(username=="admin"):
			logout(request)
			return render_to_response("index.html",context_instance=RequestContext(request))
		else:
			return HttpResponseRedirect(reverse('register:home',args=(username,)))
def login_view(request):
	global login_error
	if not request.user.is_authenticated():
		context={'error_message':login_error}
		login_error=""
		return render(request,"login.html",context)
	else:
		username=request.user.username
		return HttpResponseRedirect(reverse('register:home',args=(username,)))
	
def register(request):
	global register_error
	context={'error_message':register_error}
	register_error=""
	return render(request,"register.html", context)
def home(request,username):
	if request.user.is_authenticated():
		name=request.user.registeredclass.name
		try:
			rollno=request.user.username
			feedetail.objects.get(rollno=rollno)
			return HttpResponseRedirect(reverse('register:step2',args=(username,)))
		except ObjectDoesNotExist:
			try:
				fee=request.session['tution_fee']
				obj=feeinfo.objects.get(id=request.session['fee_id'])
				year_sem=obj.year_sem
			except KeyError:
				fee=""
				year_sem=""
			return render(request,"home.html",{"username":name,"year_sem":year_sem,"Amount":fee})
	else:
		return	redirect('/login.html') 
def registered(request):
	global register_error
	photo=request.POST.get('photo','')
	name=request.POST.get('name','')
	dob=request.POST.get('dob','')
	fname=request.POST.get('fname','')
	email_id=request.POST.get('email','')
	pass1=request.POST.get('pass1','')
	rollno_v=request.POST.get('rollno','')
	phone=request.POST.get('phn','')
	branch_v=request.POST.get('branch','')
	address_v=request.POST.get('address','')
	pincode_v=request.POST.get('pincode','')
	try:
		User.objects.create_user(rollno_v,email_id,pass1)
		userobj=User.objects.get(username=rollno_v)
		o=registeredclass					(user=userobj,name=name,branch=branch_v,mobile=phone,address=address_v,pincode=pincode_v,dob=dob,fathername=fname,photo=photo)
		o.save()
		library_obj=library_due(user=userobj,rollno=rollno_v)
		library_obj.save()	
		return redirect("/login.html")
	except IntegrityError as e:
		try:
			User.objects.get(emain_id=email)
			register_error="use another email"
		except:
			register_error="Roll No. exist"
		return redirect('/register.html')
		#return render_to_response("f.html", context_instance=RequestContext(request))


def logincheck(request):
	global login_error
	username=request.POST.get('roll','')
	password=request.POST.get('pass','')
	user=authenticate(username=username,password=password)
	if user is not None:
		if user.is_active:
			login(request,user)
			return HttpResponseRedirect(reverse('register:home',args=(username,)))		
		else:
			#return a diable account message
			login_error="your account is dissable"
			return redirect('/login.html')
			#return render(request,'login.html',{'error_message':'your account is dissable'})
	else :
		#return invalid user name or password
		login_error="invalid username or password"
		#return render(request,'login.html',{'error_message':})
		return redirect('/login.html')
def my_logout(request,username):
	logout(request)
	#redirect to success page
	return redirect('/login.html')	
	#return render_to_response("logout.html",context_instance=RequestContext(request))

def getfee(request,username):		#display the tution fee
	if request.user.is_authenticated():
		year=request.POST.get("year",'')
		#semester=request.POST.get("semester",'')
		obj=feeinfo.objects.get(year_sem=year)
		fee=obj.fee
		request.session['tution_fee']=obj.fee
		request.session['fee_id']=obj.id	
		request.session['year_sem']=obj.year_sem
		username=request.user.registeredclass.name
		return HttpResponseRedirect(reverse('register:home',args=(username,)))	
		#return render(request,"fee.html",{"year":year,"fee": fee})
	else :
			return redirect('/login.html')
def pay1(request,username):	#display tution fee payment page
	global pay_error
	if request.user.is_authenticated():
		try:	#TO check that page is requested from valid url or not
			obj=feedetail.objects.get(rollno=username)
			return render_to_response("page_except.html",context_instance=RequestContext(request))
		except ObjectDoesNotExist:
			try:
				request.session['fee_id']
				context={'error_message':pay_error}
				pay_error=""
				return render(request,"pay1.html",context)
			except KeyError:
				return HttpResponseRedirect(reverse('register:home',args=(username,)))	
	else:
		return redirect('/login.html')

def pay1check(request,username):		#pay1check used to validation of card and store information in feedetail tabel
	global pay_error
	if request.user.is_authenticated():
		card=request.POST.get("cno",'')
		month=request.POST.get("month",'')
		year=request.POST.get("year",'')
		cvv=request.POST.get("cvv",'')
		try:
			card_obj=card_detail.objects.get(cardno=card)
			if (month==card_obj.month and year==card_obj.year and cvv==card_obj.cvv):
				fee_id=request.session["fee_id"]
				feeinfo_obj=feeinfo.objects.get(id=fee_id)
				paid_amount=feeinfo_obj.fee
				rollno=request.user.username
				name=request.user.registeredclass.name
				year_sem=request.session['year_sem']
				paid_user=feedetail(user=request.user,time=date.today(),year_sem=year_sem,feeid=fee_id,rollno=rollno,name=name,Amount=paid_amount)
				paid_user.save()
				return HttpResponseRedirect(reverse('register:step2',args=(username,)))
			else:
				pay_error="invalid detail"
				return HttpResponseRedirect(reverse('register:pay1',args=(username,)))	
		except ObjectDoesNotExist:
			pay_error="Invalid card"
			return HttpResponseRedirect(reverse('register:pay1',args=(username,)))
	else:
		return redirect('/login.html')


def step2(request,username):
	if request.user.is_authenticated():
		name=request.user.registeredclass.name
		try:
			rollno=request.user.username
			hostel_fee_detail.objects.get(rollno=rollno)
			return HttpResponseRedirect(reverse('register:step3',args=(username,)))

		except ObjectDoesNotExist:
			try:
				fee=request.session['hostel_fee']
				obj=hostel_fee_info.objects.get(id=request.session['hostel_fee_id'])
				hostel=obj.hostel
			except KeyError:
				fee=""
				hostel=""
			#try:
			#	rollno=request.user.username
			#	feedetail.objects.get(rollno=rollno)
			#	return HttpResponseRedirect(reverse('register:pay1success',args=(username,)))
			#except ObjectDoesNotExist:
			return render(request,"step2.html",{"username":name,"Hostel":hostel,"Amount":fee})
	else:
		return redirect('/login.html')
def hostel_getfee(request,username):		#display the hostel fee
	if request.user.is_authenticated():
		hostel=request.POST.get("hostel",'')
		if hostel=="":
			request.session['hostel_fee']=""
		else:
			obj=hostel_fee_info.objects.get(hostel=hostel)
			request.session['hostel_fee']=obj.fee
			request.session['hostel_fee_id']=obj.id	
			request.session['hostel']=obj.hostel
		#username=request.user.registeredclass.name
		#books=request.user.registeredclass.books
		return HttpResponseRedirect(reverse('register:step2',args=(username,)))
	else:
		return redirect('/login.html')

def pay2(request,username):	#display tution fee payment page
	global pay_error
	if request.user.is_authenticated():
		try:		#TO check that page is requested from valid url or not
				obj=hostel_fee_detail.objects.get(rollno=username)
				return render_to_response("page_except.html",context_instance=RequestContext(request))
		except ObjectDoesNotExist:
				try:
					request.session['hostel_fee_id']
					context={'error_message':pay_error}
					pay_error=""
					return render(request,"pay2.html",context)
				except KeyError:
					return HttpResponseRedirect(reverse('register:step2',args=(username,)))
	else:
		return redirect('/login.html')
def pay2check(request,username):		#pay1check used to validation of card and store information in feedetail tabel
	global pay_error
	if request.user.is_authenticated():
		card=request.POST.get("cno",'')
		month=request.POST.get("month",'')
		year=request.POST.get("year",'')
		cvv=request.POST.get("cvv",'')
		try:
			card_obj=card_detail.objects.get(cardno=card)
			if (month==card_obj.month and year==card_obj.year and cvv==card_obj.cvv):
				hostel_fee_id=request.session["hostel_fee_id"]
				hostel_fee_info_obj=hostel_fee_info.objects.get(id=hostel_fee_id)
				paid_amount=hostel_fee_info_obj.fee
				rollno=request.user.username
				hostel=request.session['hostel']
				name=request.user.registeredclass.name
				paid_user=hostel_fee_detail(user=request.user,time=date.today(),feeid=hostel_fee_id,hostel=hostel,rollno=rollno,name=name,Amount=paid_amount)
				paid_user.save()
				return HttpResponseRedirect(reverse('register:step3',args=(username,)))	
			else:
				pay_error="invalid detail"
				return HttpResponseRedirect(reverse('register:pay2',args=(username,)))	
		except ObjectDoesNotExist:
			pay_error="invalid card"
			return HttpResponseRedirect(reverse('register:pay2',args=(username,)))		
	
	else:
		return redirect('/login.html')
def step3(request,username):
	if request.user.is_authenticated():
		name=request.user.registeredclass.name
		books=request.user.library_due.books
		rollno=request.user.username
		due=request.user.library_due.due
		flag=request.user.library_due.flag
		if books==0:
			if flag==0:
				if due==0:
					pay="proceed"
				else:
					pay="pay"
				o=library_due.objects.get(rollno=rollno)
				o.flag=1
				o.save()
				return render(request,"step3.html",{"username":name,"books":books,"Amount":due,"pay":pay})
			else:
				return HttpResponseRedirect(reverse('register:thanks',args=(username,)))
		else:
				return render(request,"step3_b.html",{"username":name,"books":books})
		#try:
		#	rollno=request.user.username
		#	feedetail.objects.get(rollno=rollno)
		#	return HttpResponseRedirect(reverse('register:pay1success',args=(username,)))
		#except ObjectDoesNotExist:
	else:
		return redirect('/login.html')

def pay3(request,username):	#display tution fee payment page
	global pay_error
	if request.user.is_authenticated():
			due=request.user.library_due.due
			if due==0:
				return HttpResponseRedirect(reverse('register:thanks',args=(username,)))
			else:
				context={'error_message':pay_error}
				pay_error=""
				return render(request,"pay3.html",context)
	else:
		return redirect('/login.html')	
def pay3check(request,username):		#pay1check used to validation of card and store information in feedetail tabel
	global pay_error
	if request.user.is_authenticated():
		card=request.POST.get("cno",'')
		month=request.POST.get("month",'')
		year=request.POST.get("year",'')
		cvv=request.POST.get("cvv",'')
		try:
			card_obj=card_detail.objects.get(cardno=card)
			if (month==card_obj.month and year==card_obj.year and cvv==card_obj.cvv):
				rollno=request.user.username
				obj=library_due.objects.get(rollno=rollno)
				obj.due=0
				obj.save()
				return HttpResponseRedirect(reverse('register:thanks',args=(username,)))
			else:
				pay_error="invalid detail"
				return HttpResponseRedirect(reverse('register:pay3',args=(username,)))	
		except ObjectDoesNotExist:
			pay_error="invalid card"
			return HttpResponseRedirect(reverse('register:pay3',args=(username,)))
	else:
		return redirect('/login.html')
def thanks(request,username):
	if request.user.is_authenticated():
		name=request.user.registeredclass.name
		o=request.user.feedetail
		o.flag=1
		o.save()
		return render(request,"thanks.html",{'username':name})
	else:
		return redirect('/login.html')

def print_users(request,username):
    
    # Create the HttpResponse object with the appropriate PDF headers.
   	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename=reg.pdf'
	 
	buffer = BytesIO()
	 
	report = MyPrint(buffer, 'Letter')
	pdf = report.print_canvas(request.user)
	 
	response.write(pdf)
	return response
 

def subjects_de(request,username):
	fee_id=request.session['fee_id']
	branch=request.user.registeredclass.branch
	obj=feeinfo.objects.get(id=fee_id)
	
def submit(request):
	o=feedetail.objects.filter(flag=1)
	return render(request,"submissions.html",{"student":o})