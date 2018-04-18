# # pages/views.py
import json

from django.http import HttpResponse
from django.shortcuts import render
from . models import Student
from .forms import StudentForm
from django.shortcuts import redirect
from django.db.models import Q

def index(request):
        posts = Student.objects.all()  # Getting all the posts from database
        return render(request, 'home.html', { 'posts': posts })
from django.views.decorators.csrf import csrf_exempt

def update_entry(request):
    if request.method=='GET':
        stud_id= request.GET.get('id','')
        no_of_entries = int(request.GET.get('no',''))
        stud = Student.objects.get(id=int(stud_id))
        if no_of_entries <= stud.remaining_entries:
            stud.remaining_entries =  stud.remaining_entries - no_of_entries
            stud.save()
            data = json.dumps({'allowed':no_of_entries,'denied':0})
        else:
            remaining_entries =stud.remaining_entries
            stud.remaining_entries =0
            stud.save()
            data = json.dumps({'allowed':remaining_entries,'denied':no_of_entries-remaining_entries})
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)



def get_names(request):
    if request:
        q = request.GET.get('term', '')
        students = Student.objects.filter(Q(name__icontains = q ) | Q(last_name__icontains = q ))[:20]
        results = []
        for student in students:
            autocomplete = str(student.name) +" " + str(student.middle_name)+" " + str(student.last_name)+" <" + str(student.programme) +"> id:" + str(student.id)     
            student_json = {}
            student_json['label'] = autocomplete
            student_json['id'] = student.id
            results.append(student_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

