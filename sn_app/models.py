from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField()
    address = models.URLField(max_length=500)
    email = models.EmailField()
    telephone = models.CharField(max_length=50)
    facebook_link = models.URLField(max_length=300)
    linkedin_link = models.URLField(max_length=300)
    instagram_link = models.URLField(max_length=300)
    flickr_link = models.URLField(max_length=300)
    github_link = models.URLField(max_length=300)
    twitter_link = models.URLField(max_length=300)
    skills_json = models.CharField(max_length=1000)
    hobbies_json = models.CharField(max_length=1000)

    class Meta:
        verbose_name = "Person"

    def __unicode__(self):
        return self.first_name + self.last_name

class Employer(models.Model):
    title = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
    website = models.URLField(max_length=300)
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
    description_json = models.CharField(max_length=1000)

    class Meta:
        verbose_name = "Job"
        verbose_name_plural = "Jobs"

    def __unicode__(self):
        return self.position

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
        verbose_name = "Education"
        verbose_name_plural = "Education"

    def __unicode__(self):
        return ('%s at %s, %s') % self.degree, self.college, self.end_date

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
