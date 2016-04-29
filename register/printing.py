
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from django.contrib.auth.models import User
from reportlab.pdfgen import canvas
from register.models import *
#from reportlab.pdfgen import textobject
class MyPrint:
	def __init__(self, buffer, pagesize):
		self.buffer = buffer
		if pagesize == 'A4':
		    self.pagesize = A4
		elif pagesize == 'Letter':
		    self.pagesize = letter
		self.width, self.height = self.pagesize
	def print_canvas(self,cur_user):
		buffer=self.buffer
		rollno=cur_user.username
		name=cur_user.registeredclass.name
		fathername=cur_user.registeredclass.fathername
		mobile=cur_user.registeredclass.mobile
		address=cur_user.registeredclass.address
		dob=cur_user.registeredclass.dob
		pin=cur_user.registeredclass.pincode
		branch=cur_user.registeredclass.branch
		#tution fee detail
		fee_id=cur_user.feedetail.id
		fee_id1=cur_user.feedetail.feeid
		amount=cur_user.feedetail.Amount
		year_sem=cur_user.feedetail.year_sem
		time=cur_user.feedetail.time

		#hostel fee detail

		hostel_fee_id=cur_user.hostel_fee_detail.feeid
		hostel=cur_user.hostel_fee_detail.hostel
		hamount=cur_user.hostel_fee_detail.Amount
		#SUBJECTS DETAIL
		sub_obj=feeinfo.objects.get(id=fee_id1)
		query=sub_obj.subjects_detail_set.filter(branch=branch)
		#printing pdf
		c = canvas.Canvas(buffer, pagesize=letter)
		c.setLineWidth(.3)
		c.setFont('Helvetica', 15)
		c.drawString(100,770,'NATIONAL INSTITUTE OF TECHNOLOGY HAMIRPUR')
		ch=30 
		c.drawString(230,770-ch,'REGISTRATION FORM')
		c.setFont('Helvetica', 8)
		c.drawString(210,735-ch,'SESSION')
		c.drawString(250,735-ch,'2016-2017')
		c.line(250,732-ch,300,732-ch)
		c.drawString(30,735-ch,'ROLL NO.')
		c.drawString(80,735-ch,rollno)
		c.line(80,732-ch,120,732-ch)
		c.drawString(350,735-ch,'BRANCH:')
		c.line(400,732-ch,580,732-ch)
		c.drawString(400,735-ch,branch)
		c.drawString(350,720-ch,'YEAR/SEM:')
		c.line(400,717-ch,580,717-ch)
		c.drawString(400,720-ch,year_sem)
		c.drawString(30,703-ch,'NAME:')
		c.drawString(120,703-ch,name)
		c.drawString(30,686-ch,'FATHER NAME:')
		c.drawString(120,686-ch,fathername)
		c.drawString(30,669-ch,'DOB:')
		c.drawString(120,666-ch,dob)
		c.drawString(30,652-ch,'ADDRESS:')
		textobject = c.beginText(120,649-ch)
		textobject.textOut(address)
		c.drawText(textobject)
		c.drawString(30,635-ch,'MOBILE:')
		c.drawString(120,635-ch,mobile)
		c.drawString(500,635-ch,'PIN:')
		c.drawString(530,635-ch,pin)
		#Tution fee detail
		c.setLineWidth(.3)
		c.setFont('Helvetica', 12)
		c.drawString(30,600-ch,'TUTION FEE DETAIL-')
		c.setLineWidth(.3)
		c.setFont('Helvetica', 8)
		c.drawString(40,583-ch,'AMOUNT:')
		c.drawString(130,583-ch,str(amount))
		c.drawString(40,566-ch,'TRANSACTION TIME:')
		c.drawString(130,566-ch,str(time))
		c.drawString(40,549-ch,'TRANSACTION ID:')
		c.drawString(130,549-ch,str(fee_id))
		#hostel fee detail
		c.setLineWidth(.3)
		c.setFont('Helvetica', 12)
		c.drawString(30,514-ch,'HOSTEL FEE DETAIL-')
		c.setLineWidth(.3)
		c.setFont('Helvetica', 8)
		c.drawString(40,497-ch,'AMOUNT:')
		c.drawString(130,497-ch,str(amount))
		c.drawString(40,480-ch,'TRANSACTION TIME:')
		c.drawString(130,480-ch,str(time))
		c.drawString(40,463-ch,'TRANSACTION ID:')
		c.drawString(130,463-ch,str(fee_id))
		c.setFont('Helvetica', 12)
		c.drawString(30,428-ch,'LIBRARY DUES-')
		c.setFont('Helvetica', 8)
		c.drawString(40,411-ch,'STATUS: ')
		c.drawString(130,411-ch,'Clear')
		c.setFont('Helvetica', 12)
		c.drawString(30,377-ch,'SUBJECTS DETAIL-')
		c.setFont('Helvetica', 8)
		c.drawString(30,360-ch,'CODE')
		c.drawString(70,360-ch,'L')
		c.drawString(90,360-ch,'T')
		c.drawString(110,360-ch,'P')
		c.drawString(130,360-ch,'C')
		c.drawString(169,360-ch,'SUBJECTS')
		dis=17
		sum1=0
		sum2=0
		sum3=0
		sum4=0
		for i in range(query.count()):
			l=query[i].lectures
			t=query[i].tutorials
			p=query[i].practicals
			cd=query[i].credits
			c.drawString(30,360-dis-ch,query[i].code)
			c.drawString(70,360-dis-ch,str(l))
			c.drawString(90,360-dis-ch,str(t))
			c.drawString(110,360-dis-ch,str(p))
			c.drawString(130,360-dis-ch,str(cd))
			textobject = c.beginText(150,360-dis-ch)
			textobject.textOut(query[i].subjects)
			c.drawText(textobject)
			sum1+=l
			sum2+=t
			sum3+=p
			sum4+=cd
			dis+=17
		c.drawString(30,360-dis-ch,'TOTAL')
		c.drawString(70,360-dis-ch,str(sum1))
		c.drawString(90,360-dis-ch,str(sum2))
		c.drawString(110,360-dis-ch,str(sum3))
		c.drawString(130,360-dis-ch,str(sum4))
		c.drawString(300,360-dis-ch-17,'SIGNATURE OF APPLICANT:')
		c.line(450,360-dis-ch-17,580,360-dis-ch-17)
		c.showPage()
		c.save()
		pdf=buffer.getvalue()
		buffer.close()
		return pdf
