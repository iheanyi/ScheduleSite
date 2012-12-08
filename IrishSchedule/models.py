from django.db import models
import re
import requests
from BeautifulSoup import BeautifulSoup

# Create your models here.

class Department(models.Model):
	deptname = models.CharField("Department Name", max_length = 200)
	deptkey = models.CharField("Department Tag", max_length = 10, primary_key = True)

	def __unicode__(self):
		return self.deptkey

	def post_request(self):
		print self.deptkey
		payload = {'TERM':'201220', 'DIVS': 'A', 'CAMPUS':'M', 'SUBJ':self.deptkey, 'ATTR':'0ANY', 'CREDIT':'A' }
		r = requests.post("https://was.nd.edu/reg/srch/ClassSearchServlet", data=payload)
			#print r.text
			#print r.status_code

		html = r.text
		if(len(html) > 30000):
			self.add_course(html)

	def add_course(self, html):
		soup = BeautifulSoup(html)

		result_table = soup.find('table', {'id': 'resulttable'})
		body_result = result_table.find('tbody')

		#select = soup.find('select', {'name': 'SUBJ'})
		prev = None

		for row in body_result.findAll('tr'):
			cells = row.findAll('td')

			section = cells[0].text.partition('-')[2]
			course = cells[0].text.partition('-')[0]

			section = re.sub('[^0-9]', '', section)
			course = re.sub('[^A-Za-z0-9]+', '', course)

			print course

			title = cells[1].text
			credits = cells[2].text
			max_spots = cells[4].text
			open_spots = cells[5].text
			crn = cells[7].text
			instructor = cells[9].text
			time = cells[10].text
			location = cells[13].text


			# Fix inconsistencies in the title of some courses . . . 
			if course == prev:
				title = old_title
				credits = old_credits



		 	c = Course.objects.get_or_create(title=title, credits = credits, course_no = course, department = self)
			
			s = Section.objects.get_or_create(section_num = section, open_spots = open_spots, max_spots = max_spots, crn = crn, instructor = instructor, time = time, location = location, course = c[0])
			# if title == prev:
			# 	sect = Section(section_num = section, open_spots = open_spots, max_spots = max_spots, crn = crn, instructor = instructor, time = time, location = time, Course = cour)
				
			# 	sect.save()
			# 	self.CourseList[-1].add(s)

			# else:
			# 	c = CoursePy(title, credits, course)
			# 	s = SectionPy(section, open_spots, max_spots, crn, instructor, time, location)

			# 	cour = Course(title = title, credits = credits, course = course, department = d)
			# 	cour.save()
			# 	sect = Section(section_num = section, open_spots = open_spots, max_spots = max_spots, crn = crn, instructor = instructor, time = time, location = time, Course = cour)
			# 	sect.save()
			# 	c.add(s)
			# 	self.add(c)

			if course is not None:
			 	prev = course
			 	old_title = title
			 	old_credits = credits
 
class Course(models.Model):
	department = models.ForeignKey(Department)
	title = models.CharField("Course Title", max_length = 200)
	credits = models.CharField("Number of Credits", max_length = "3")
	course_no = models.CharField("Course Number", max_length = 15, primary_key = True)

	def __unicode__(self):
		return u"%s - %s" % (self.course_no, self.title)

class Section(models.Model):
	course = models.ForeignKey(Course)
	section_num = models.IntegerField("Section Number")
	open_spots = models.IntegerField("Open Number of Spots")
	max_spots = models.IntegerField("Maximum Number of Spots")
	instructor = models.CharField("Section Instructor", max_length = 200)
	time = models.CharField("Section Time", max_length = 50)
	location = models.CharField("Section Location", max_length = 200)
	crn = models.CharField("Course Registration Number", max_length = 5, primary_key = True)

	def __unicode__(self):
		return u"Section %d (%s) : with %s on %s at %s (%d/%d spots)" % (self.section_num, self.crn, self.instructor, self.time, self.location, self.open_spots, self.max_spots)