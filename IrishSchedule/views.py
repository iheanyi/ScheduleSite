# Create your views here.
from django.http import HttpResponse, Http404
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404

from IrishSchedule.models import Department, Course, Section


def index(request):

	department_list = Department.objects.all()
	#template = loader.get_template('courses/index.html')

	context = {'department_list': department_list}
	return render(request, 'courses/index.html', context)

def courses(request, deptkey):
	#print deptkey
	#dept = get_object_or_404(Department, deptkey=deptkey)
	#dept = get_object_or_404(Department, deptkey)
	#print dept.course_set.all()
	#deptkey = deptkey[0:-1]
	course_list = Course.objects.filter(department = deptkey)

	context = {'course_list': course_list}

	return render(request, 'courses/courses.html', context)

def sections(request, course_no):
	section_list = Section.objects.filter(course = course_no)

	context = {'section_list': section_list}
	return render(request, 'courses/sections.html', context)