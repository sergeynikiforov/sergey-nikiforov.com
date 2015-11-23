from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
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
    view to handle ajax contact form
    '''
    person = get_object_or_404(Person, first_name='Sergey')
    # if it's a POST request
    if request.method == 'POST':

        # create a form
        form = ContactMeForm(request.POST)
        # for response json
        response_data = {}

        # check validity
        if form.is_valid():
            # save the form
            form.save()

            # add success message
            #messages.add_message(request, messages.SUCCESS, 'Your message has been sent. Thank you!')

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
            #return redirect('sn_app:contact')
            response_data['result'] = 'Your message has been sent. Thank you!'

            return JsonResponse(response_data)
        else:
            # just print to terminal
            response_data['result'] = form.errors
            print(form.errors)
            return JsonResponse(response_data)
    else:
        # GET request - create empty form
        form = ContactMeForm()

    return render(request, 'sn_app/contact.html', {'form': form, 'person': person})


def photoset(request, photoset_slug='test'):
    '''
    view for a particular photoset page (thumbnails view)
    '''
    # create context dict
    context_dict = {}

    # get all photosets for navigation
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

    return render(request, 'sn_app/photoset.html', context_dict)


def photography(request):
    '''
    view for photography page (with thumbs for photosets)
    '''
    # create context dict
    context_dict = {}

    # get all photosets
    photosets = Photoset.objects.all().order_by('title')
    context_dict['photosets'] = photosets

    # get personal data
    person = get_object_or_404(Person, first_name='Sergey')
    context_dict['person'] = person

    return render(request, 'sn_app/photography.html', context_dict)


def photo(request, photoset_slug='', photoID=''):
    '''
    view for a particular photograph
    '''

    context_dict = {}

    # pass chosen photo
    context_dict['photoID'] = photoID

    # increment photo views counter
    current_photo = Photo.objects.get(publicID=photoID)
    context_dict['current_photo'] = current_photo
    current_photo.num_views += 1
    current_photo.save()

    # get relevant photoset
    try:
        # add photoset to context dict
        active_photoset = Photoset.objects.get(slug=photoset_slug)
        context_dict['active_photoset'] = active_photoset

        # retrieve prev/next photoID's for the current photo
        photos = Photo.objects.filter(photosets__title__exact=active_photoset.title).values_list('id', 'publicID').order_by('id')
        photos = [i[1] for i in photos]
        qty = len(photos)
        context_dict['prev_photoID'] = photos[(photos.index(photoID) - 1) % qty]
        context_dict['next_photoID'] = photos[(photos.index(photoID) + 1) % qty]

    except Photoset.DoesNotExist, Photo.DoesNotExist:
        pass

    # get all photosets
    photosets = Photoset.objects.all().order_by('title')
    context_dict['photosets'] = photosets

    # get personal data
    person = get_object_or_404(Person, first_name='Sergey')
    context_dict['person'] = person

    return render(request, 'sn_app/photo.html', context_dict)