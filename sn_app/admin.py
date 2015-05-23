from django.contrib import admin
import models

class PersonAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Bio', {'fields': ['first_name', 'last_name', 'birthdate']}),
        ('Contact Info', {'fields': ['address', 'telephone', 'email']}),
        ('Social Networks', {'fields': ['facebook_link', 'linkedin_link', 'instagram_link', 'flickr_link', 'github_link', 'twitter_link']}),
        ('Other', {'fields': ['skills_json', 'hobbies_json']})
    ]

class ContactMeAdmin(admin.ModelAdmin):
    list_display = ('sender_name', 'sender_email', 'time_sent')

admin.site.register(models.Person, PersonAdmin)
admin.site.register(models.Employer)
admin.site.register(models.Job)
admin.site.register(models.Education)
admin.site.register(models.OnlineCourse)
admin.site.register(models.ContactMe, ContactMeAdmin)
