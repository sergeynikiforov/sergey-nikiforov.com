from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from models import Person, Education, Job, OnlineCourse, Photo, PhotoInPhotoset, Photoset
from forms import ContactMeForm
import json


def resume(request):
    '''
    view for resume page
    '''
    # get data from db
    person = get_object_or_404(Person, first_name='Sergey')
    jobs = Job.objects.filter(person=person).order_by('-end_date')
    education = Education.objects.filter(person=person).order_by('-end_date')
    onlinecourses = OnlineCourse.objects.filter(person=person)

    # construct dict containing job achievements from json
    if jobs:
        achievements_dict = {}
        for job in jobs:
            achievements_dict[job.position] = json.loads(job.achievements_json)

    # get dict with skills
    if person:
        skills = json.loads(person.skills_json)

    # context dictionary to pass to template
    context_dict = {
        'person': person,
        'jobs': jobs,
        'education': education,
        'onlinecourses': onlinecourses,
        'achievements': achievements_dict,
        'skills': skills
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
    '''
    view for about page
    '''
    # get personal data
    person = get_object_or_404(Person, first_name='Sergey')

    # get skills and hobbies
    personal = {}
    personal['skills'] = json.loads(person.skills_json)
    personal['hobbies'] = json.loads(person.hobbies_json)

    # context dictionary to pass to template
    context_dict = {
        'person': person,
        'personal': personal
    }
    return render(request, 'sn_app/about.html', context_dict)

def contact(request):
    '''
    view to handle contact form
    '''
    person = get_object_or_404(Person, first_name='Sergey')
    # if it's a POST request
    if request.method == 'POST':
        # create a form
        form = ContactMeForm(request.POST)
        # check validity
        if form.is_valid():
            # save the form
            form.save()
            # add success message
            messages.add_message(request, messages.SUCCESS, 'Thank you for your message!')
            # construct email for site owner (me)
            body = "You've got a message from %s (%s):\n\n%s\n\n---END OF MESSAGE---\n" % (form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['message'])
            reply_to = form.cleaned_data['email']
            email = EmailMessage(
                                 subject='[Django] - You have 1 new message',
                                 body=body,
                                 to=('serge.a.nikiforov@gmail.com',),
                                 reply_to=(reply_to,)
                                )
            email.send()
            return redirect('sn_app:contact')
        else:
            # just print to terminal
            print(form.errors)
    else:
        # GET request - create empty form
        form = ContactMeForm()

    return render(request, 'sn_app/contact.html', {'form': form, 'person': person})

def photography(request, photoset_slug='test'):
    '''
    view for photography page
    '''
    # old flickr implementation
    '''
    # authenticate via flickr_api
    flickr_api.set_auth_handler('auth.txt')

    # get the authenticated user
    user = flickr_api.test.login()

    # get photos
    albums = {}
    photosets = user.getPhotosets()

    albums[photosets[1].title] = [x.getSizes()['Large']['source'] for x in photosets[1].getPhotos()]

    urlp = photosets[2].getPhotos()[7].getSizes()['Large']['source']
    '''
    # create context dict
    context_dict = {}

    # get all photosets
    photosets = Photoset.objects.all().order_by('title')
    context_dict['photosets'] = photosets

    # get active photoset
    try:
        active_photoset = Photoset.objects.get(slug=photoset_slug)
        context_dict['photoset_title'] = active_photoset.title

        # get description if not none
        if active_photoset.description != 'none':
            context_dict['photoset_description'] = active_photoset.description

        # retrieve photos for the active photoset
        photos = Photo.objects.filter(photosets__title__exact=active_photoset.title)
        context_dict['photos'] = photos

        # add photoset to context dict
        context_dict['active_photoset'] = active_photoset

        # increment views counter
        active_photoset.num_views += 1
        active_photoset.save()

    except Photoset.DoesNotExist:
        pass

    # get personal data
    person = get_object_or_404(Person, first_name='Sergey')
    context_dict['person'] = person

    return render(request, 'sn_app/photography.html', context_dict)
