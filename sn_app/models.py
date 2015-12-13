from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
#import datetime


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField()
    address = models.CharField(max_length=500)
    email = models.EmailField()
    telephone = models.CharField(max_length=50)
    facebook_link = models.URLField(max_length=300)
    linkedin_link = models.URLField(max_length=300)
    instagram_link = models.URLField(max_length=300)
    flickr_link = models.URLField(max_length=300)
    github_link = models.URLField(max_length=300)
    twitter_link = models.URLField(max_length=300)
    skills_json = models.TextField(max_length=1000)
    hobbies_json = models.TextField(max_length=1000)

    class Meta:
        verbose_name = "Person"

    def __unicode__(self):
        return self.first_name + self.last_name


class Employer(models.Model):
    title = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
    website = models.URLField(max_length=300)
    description = models.TextField(max_length=1000)
    number_of_employees = models.IntegerField()

    class Meta:
        verbose_name = "Employer"
        verbose_name_plural = "Employers"

    def __unicode__(self):
        return self.title


class Job(models.Model):
    employer = models.ForeignKey(Employer)
    person = models.ForeignKey(Person)
    position = models.CharField(max_length=300)
    start_date = models.DateField()
    end_date = models.DateField()
    achievements_json = models.TextField(max_length=1000)

    class Meta:
        verbose_name = "Job"
        verbose_name_plural = "Jobs"

    def __unicode__(self):
        return self.position

    def workterm(self):
        return self.end_date - self.start_date


class Education(models.Model):
    person = models.ForeignKey(Person)
    college = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
    website = models.URLField(max_length=300)
    degree = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        verbose_name = "Education entry"
        verbose_name_plural = "Education entries"

    def __unicode__(self):
        return "%s at %s, %s" % (self.degree, self.college, self.end_date.year)


class OnlineCourse(models.Model):
    person = models.ForeignKey(Person)
    title = models.CharField(max_length=500)
    school = models.CharField(max_length=500)
    date = models.DateField()
    url = models.URLField(max_length=300)

    class Meta:
        verbose_name = "Online Course"
        verbose_name_plural = "Online Courses"

    def __unicode__(self):
        return self.title


class ContactMe(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=2000)
    time_sent = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "ContactMe message"
        verbose_name_plural = "ContactMe messages"

    def __unicode__(self):
        # localtime() to display time in current timezone
        return '%s at %s' % (self.name, timezone.localtime(self.time_sent))


class Photoset(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=2000)
    short_description = models.TextField(max_length=1000, default='Vehicula sem libero per ipsum donec, ante vitae neque mauris, integer quisque et nisl, etiam veritatis pede commodo sed penatibus vel, erat ac suspendisse ipsum enim tristique orci.')
    cover_photo = models.OneToOneField('Photo', null=True) # Photo model instance
    num_views = models.PositiveIntegerField(default=0)
    num_photos = models.PositiveIntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Photoset, self).save(*args, **kwargs)

    def __unicode__(self):
        return '"%s" photoset with %i photos, viewed %i time(s)' % (self.title, self.num_photos, self.num_views)


class Photo(models.Model):
    publicID = models.CharField(max_length=200)  # Cloudinary photo publicID
    url = models.URLField(default='http://www.example.com')
    title = models.CharField(max_length=200, default='Untitled')
    description = models.TextField(max_length=2000, default='No description')
    date_taken = models.DateTimeField(default=timezone.now)
    num_views = models.PositiveIntegerField(default=0)
    photosets = models.ManyToManyField(Photoset, through='PhotoInPhotoset')

    def __unicode__(self):
        return '"%s" photo %s, viewed %i time(s)' % (self.title, self.publicID, self.num_views)


class PhotoInPhotoset(models.Model):
    photoset = models.ForeignKey(Photoset)
    photo = models.ForeignKey(Photo)
    order = models.FloatField()

    def save(self, *args, **kwargs):
        self.photoset.num_photos += 1
        self.photoset.save()
        super(PhotoInPhotoset, self).save(*args, **kwargs)
