from django.shortcuts import render
from models import Person, Education, Job, OnlineCourse
import json

def landing(request):
    # get data from db
    person = Person.objects.get(first_name='Sergey')
    jobs = Job.objects.filter(person=person).order_by('-end_date')
    education = Education.objects.filter(person=person).order_by('-end_date')
    onlinecourses = OnlineCourse.objects.filter(person=person)

    # construct dict containing job achievements from json
    achievements_dict = {}
    for job in jobs:
        achievements_dict[job.position] = json.loads(job.achievements_json)

    # context dictionary to pass to template
    context_dict = {
        'person': person,
        'jobs': jobs,
        'education': education,
        'onlinecourses': onlinecourses,
        'achievements': achievements_dict
        }
    return render(request, 'sn_app/index.html', context_dict)
