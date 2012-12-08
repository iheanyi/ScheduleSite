#from django.db import models
from django.core.management.base import BaseCommand, CommandError
from IrishSchedule.models import Department, Course, Section
import mechanize
#import os
#os.environ['DJANGO_SETTINGS_MODULE'] = "myproject.settings"

class Command(BaseCommand):

	def handle(self, *args, **options):
		br = mechanize.Browser()
		br.set_handle_equiv(True)
		#br.set_handle_gzip(True)
		br.set_handle_redirect(mechanize.HTTPRedirectHandler)
		br.set_handle_referer(True)

		br.open("https://was.nd.edu/reg/srch/ClassSearchServlet")

		forms = [f for f in br.forms()]
		subj_form = forms[0]

		control = subj_form.find_control("SUBJ")

		for item in control.items:
			#item.selected = False
			#print item.attrs['label'] + item.name
			d = Department.objects.get_or_create(deptname=item.attrs['label'], deptkey=item.name)
			print d[0]
			#print d[1]
			d[0].post_request()

			item.selected = False
			#yaml.dump(dept, sys.stdout)

