from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.template.loader import get_template
from models import Person, Education, Job, OnlineCourse, Photo, PhotoInPhotoset, Photoset
from forms import ContactMeForm
import json
import cloudinary



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


def photo_home(request, photoset_slug):
    '''
    view for home page photo_api
    '''

    context_dict = {}

    # add photoset to context dict
    active_photoset = get_object_or_404(Photoset, slug=photoset_slug)
    context_dict['active_photoset'] = active_photoset

    # get all photosets
    photosets = Photoset.objects.all().order_by('title')
    context_dict['photosets'] = photosets

    # get personal data
    person = get_object_or_404(Person, first_name='Sergey')
    context_dict['person'] = person

    return render(request, 'sn_app/photo-home.html', context_dict)


def photo_dict(photoset_slug='', photoID='', srcset="200w 400w 600w 800w 1000w 1200w 1400w 1600w 2000w 2400w 2800w 3200w"):
    '''
    returns dict photo info
    '''
    context_dict = {}

    # pass chosen photo
    context_dict['id'] = photoID

    # increment photo views counter & populate context
    current_photo = Photo.objects.get(publicID=photoID)

    context_dict['photoset'] = photoset_slug
    context_dict['title'] = current_photo.title
    context_dict['description'] = current_photo.description

    current_photo.num_views += 1
    current_photo.save()

    # get prev/next photoID
    try:
        active_photoset = Photoset.objects.get(slug=photoset_slug)
        photos = Photo.objects.filter(photosets__title__exact=active_photoset.title).values_list('id', 'publicID').order_by('id')
        photos = [i[1] for i in photos]
        qty = len(photos)
        context_dict['prev_photoID'] = photos[(photos.index(photoID) - 1) % qty]
        context_dict['next_photoID'] = photos[(photos.index(photoID) + 1) % qty]

    except Photoset.DoesNotExist, Photo.DoesNotExist:
        pass

    # populate with info for <picture> elt
    srcsetWebp = ''
    srcsetJpg = ''
    srcset = srcset.split()

    # construct srcset for Webp & jpeg images
    for src in srcset:
        width = int(src[:-1])
        srcsetWebp += '{photo_url} {src_width}, '.format(photo_url=cloudinary.CloudinaryImage(photoID).build_url(format="webp", width=width, crop="fill", quality=85), src_width=src)
        srcsetJpg += '{photo_url} {src_width}, '.format(photo_url=cloudinary.CloudinaryImage(photoID).build_url(format="jpg", width=width, crop="fill", quality=85), src_width=src)

    srcsetWebp = srcsetWebp[:-2]
    srcsetJpg = srcsetJpg[:-2]
    imgSrc = cloudinary.CloudinaryImage(photoID).build_url(format="jpg", width=1024, crop="fill")

    context_dict['srcsetWebp'] = srcsetWebp
    context_dict['srcsetJpg'] = srcsetJpg
    context_dict['imgSrc'] = imgSrc

    return context_dict


def photo_api(request, photoset_slug='', photoID=''):
    '''
    view for a single photo response
    '''

    context_dict = photo_dict(photoset_slug=photoset_slug, photoID=photoID)

    return JsonResponse(context_dict)


def photoset_api(request, photoset_slug=''):
    '''
    view for a photoset response
    '''
    # get all photos for the photoset
    active_photoset = Photoset.objects.get(slug=photoset_slug)
    photos = Photo.objects.filter(photosets__title__exact=active_photoset.title).order_by('id')
    result = [photo_dict(photoset_slug=photoset_slug, photoID=x.publicID) for x in photos]

    return JsonResponse({'models': result})


def photoset(request, photoset_slug=''):
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
    view for a general photography page (with thumbs for photosets)
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
