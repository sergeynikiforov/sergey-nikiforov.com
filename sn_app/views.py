from django.shortcuts import render
from models import Person, Education, Job, OnlineCourse
import json

def resume(request):
    '''
    view for resume page
    '''
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
    return render(request, 'sn_app/resume.html', context_dict)

def landing(request):
    '''
    view for landing page
    '''
    # get personal data
    person = Person.objects.get(first_name='Sergey')

    # context dictionary to pass to template
    context_dict = {
        'person': person
    }
    return render(request, 'sn_app/landing.html', context_dict)

def about(request):
    pass
