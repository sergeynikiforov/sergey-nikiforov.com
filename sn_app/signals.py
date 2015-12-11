from models import PhotoInPhotoset
from django.db.models.signals import post_delete
from django.dispatch import receiver

# decrement num_photos counter when deleting Photo/PhotoInPhotoset instance
@receiver(post_delete, sender=PhotoInPhotoset)
def photoset_post_delete(sender, **kwargs):
    kwargs['instance'].photoset.num_photos -= 1
    kwargs['instance'].photoset.save()