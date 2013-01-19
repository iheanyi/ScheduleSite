from django.core import serializers
from django.core.management.base import BaseCommand, CommandError
from IrishSchedule.models import Department, Course, Section

class Command(BaseCommand):

	def handle(self, *args, **options):
		ddata = serializers.serialize("json", Department.objects.all(), indent=4)
		cdata = serializers.serialize("json", Course.objects.all(), indent=4)
		sdata = serializers.serialize('json', Section.objects.all(), indent=4)
		dout = open("IrishSchedule/export/departments.json", "w")
		cout = open("IrishSchedule/export/courses.json", "w")
		sout = open("IrishSchedule/export/sections.json", "w")
		dout.write(ddata)
		dout.close()
		cout.write(cdata)
		cout.close()
		sout.write(sdata)
		sout.close()