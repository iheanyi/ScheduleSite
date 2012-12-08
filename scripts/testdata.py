#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file has been automatically generated, changes may be lost if you
# go and generate it again. It was generated with the following command:
# manage.py dumpscript IrishSchedule
#
# to restore it, run
# manage.py runscript module_name.this_script_name 
#
# example: if manage.py is at ./manage.py
# and the script is at ./some_folder/some_script.py
# you must make sure ./some_folder/__init__.py exists
# and run  ./manage.py runscript some_folder.some_script

import datetime
import requests
import mechanize
from BeautifulSoup import BeautifulSoup
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType

def run():
    #initial imports

    def locate_object(original_class, original_pk_name, the_class, pk_name, pk_value, obj_content):
        #You may change this function to do specific lookup for specific objects
        #
        #original_class class of the django orm's object that needs to be located
        #original_pk_name the primary key of original_class
        #the_class      parent class of original_class which contains obj_content
        #pk_name        the primary key of original_class
        #pk_value       value of the primary_key
        #obj_content    content of the object which was not exported.
        #
        #you should use obj_content to locate the object on the target db    
        #
        #and example where original_class and the_class are different is
        #when original_class is Farmer and
        #the_class is Person. The table may refer to a Farmer but you will actually
        #need to locate Person in order to instantiate that Farmer
        #
        #example:
        #if the_class == SurveyResultFormat or the_class == SurveyType or the_class == SurveyState:        
        #    pk_name="name"
        #    pk_value=obj_content[pk_name]
        #if the_class == StaffGroup:
        #    pk_value=8
            
        search_data = { pk_name: pk_value }
        the_obj =the_class.objects.get(**search_data)
        #print the_obj
        return the_obj    



    #Processing model: Department

    from IrishSchedule.models import Department


    #Processing model: Course

    from IrishSchedule.models import Course


    #Processing model: Section

    from IrishSchedule.models import Section

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
        dept = Department(item.attrs['label'], item.name)
        #dept.getInfo(br)
        dept.postRequest()
        f = open('data.json', 'a')
        f.write(simplejson.dumps(simplejson.loads(pickled),indent=4))
        #print pickled
        #print json.dumps(dept)
        #pprint(vars(dept.CourseList[1].sections[0]), indent=4)
        departments.append(dept)
        item.selected = False
        #yaml.dump(dept, sys.stdout)

    f.close
    for d in departments:
        yaml.dump(d, sys.stdout)