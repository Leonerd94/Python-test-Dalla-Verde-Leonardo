from django.shortcuts import render
from enrolment.models import student
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import datetime as d
from django.utils.timezone import utc

# Create your views here.

@csrf_exempt
def home(request):
	if request.method == 'POST':
		body = request.body
		content = json.loads(body)
		stud = student(
						fname=content['fname'],
						lname=content['lname'],
						dt=d.datetime.now(utc))
		stud.save()
		return HttpResponse(status=200)
	elif request.method == 'GET':
		stud = student.objects.all()
		list_stud = [{'fname':x.fname, 'lname':x.lname, 'dt':str(x.dt)} for x in stud]
		resp = json.dumps(list_stud)

		return HttpResponse(resp, content_type='application/json')