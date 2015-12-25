from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.core.mail import EmailMessage
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
    view for home page photo_api - single photo view

    returns in context:
    - active photoset
    - all 'photosets'
    - person
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


def photo_dict(photoset, photo, srcset="200w 400w 600w 800w 1000w 1200w 1400w 1600w 2000w 2400w 2800w 3200w"):
    '''
    helper function, returns dict photo info

    photoset: current photoset from django ORM
    photo: current photo from django ORM
    '''
    context_dict = {}

    # pass chosen photo
    context_dict['id'] = photo.publicID

    context_dict['photoset'] = photoset.title
    context_dict['title'] = photo.title
    context_dict['description'] = photo.description
    context_dict['year'] = photo.date_taken.year

    # get prev/next photoID + order info
    try:
        photos = PhotoInPhotoset.objects.filter(photoset=photoset).order_by('order')
        photos = [i.photo.publicID for i in photos]
        qty = len(photos)
        current_photo_index = photos.index(photo.publicID)
        context_dict['order'] = '{current} / {total}'.format(current=current_photo_index+1, total=photoset.num_photos)
        context_dict['prev_photoID'] = photos[(current_photo_index - 1) % qty]
        context_dict['next_photoID'] = photos[(current_photo_index + 1) % qty]

    except Photoset.DoesNotExist, Photo.DoesNotExist:
        pass

    # populate with info for <picture> elt
    srcsetWebp = ''
    srcsetJpg = ''
    srcset = srcset.split()

    # construct srcset for Webp & jpeg images
    for src in srcset:
        width = int(src[:-1])
        srcsetWebp += '{photo_url} {src_width}, '.format(photo_url=cloudinary.CloudinaryImage(photo.publicID).build_url(format="webp", width=width, crop="fill", quality=85), src_width=src)
        srcsetJpg += '{photo_url} {src_width}, '.format(photo_url=cloudinary.CloudinaryImage(photo.publicID).build_url(format="jpg", width=width, crop="fill", quality=85), src_width=src)

    srcsetWebp = srcsetWebp[:-2]
    srcsetJpg = srcsetJpg[:-2]
    imgSrc = cloudinary.CloudinaryImage(photo.publicID).build_url(format="jpg", width=1024, crop="fill")

    context_dict['srcsetWebp'] = srcsetWebp
    context_dict['srcsetJpg'] = srcsetJpg
    context_dict['imgSrc'] = imgSrc

    return context_dict


def photo_api(request, photoset_slug='', photoID=''):
    '''
    view for a single photo response
    '''

    current_photo = Photo.objects.get(publicID=photoID)
    current_photo.num_views += 1
    current_photo.save()

    active_photoset = Photoset.objects.get(slug=photoset_slug)

    context_dict = photo_dict(active_photoset, current_photo)

    return JsonResponse(context_dict)


def photoset_api(request, photoset_slug=''):
    '''
    view for a photoset response
    '''
    # get all photos for the photoset
    active_photoset = Photoset.objects.get(slug=photoset_slug)
    photos = Photo.objects.filter(photosets__title__exact=active_photoset.title).order_by('id')

    result = [photo_dict(active_photoset, photo) for photo in photos]

    return JsonResponse({'models': result})


def photoset(request, photoset_slug=''):
    '''
    view for a particular photoset page (thumbnails view)

    returns in context:
    - all photosets in 'photosets'
    - current 'photoset_title' & 'photoset_description'
    - the whole 'active_photoset'
    - 'photos' of current photoset
    - 'person'
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
        photos_in_photoset = PhotoInPhotoset.objects.filter(photoset=active_photoset).order_by('order')
        for index, photo_in_photoset in enumerate(photos_in_photoset):
            photo_in_photoset.photo.current_order = index + 1
        photos = [i.photo for i in photos_in_photoset]
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

    returns in context:
    - all photosets in 'photosets'
    - 'person'
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


def my_page_not_found_view(request):
    '''
    Custom 404 view
    '''
    # create context dict
    context_dict = {}

    # get personal data
    person = Person.objects.get(first_name='Sergey')

    context_dict['person'] = person

    return render(request, 'sn_app/404.html', context_dict)


def my_error_view(request):
    '''
    Custom 500 view
    '''
    # create context dict
    context_dict = {}

    # get personal data
    person = Person.objects.get(first_name='Sergey')

    context_dict['person'] = person

    return render(request, 'sn_app/500.html', context_dict)


def my_permission_denied_view(request):
    '''
    Custom 403 view
    '''
    # create context dict
    context_dict = {}

    # get personal data
    person = Person.objects.get(first_name='Sergey')

    context_dict['person'] = person

    return render(request, 'sn_app/403.html', context_dict)


def my_bad_request_view(request):
    '''
    Custom 400 view
    '''
    # create context dict
    context_dict = {}

    # get personal data
    person = Person.objects.get(first_name='Sergey')

    context_dict['person'] = person

    return render(request, 'sn_app/400.html', context_dict)


def test(request):
    '''
    view for test page
    '''
    # get personal data
    person = Person.objects.get(first_name='Sergey')

    # context dictionary to pass to template
    context_dict = {
        'person': person
    }

    return render(request, 'sn_app/test.html', context_dict)