# set django config
import os
import sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sn_project.settings')

import django
django.setup()

# import needed models
from sn_app.models import Photo, Photoset, PhotoInPhotoset

# import Cloudinary classes
import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinaryconfig import cloud_name, api_key, api_secret

# set Cloudinary configuration
cloudinary.config(
  cloud_name = cloud_name,
  api_key = api_key,
  api_secret = api_secret
)

# path to dir containing photos
photopath = '/home/sergeynikiforov/Dropbox/img_assets/test/'

def populate(photos_path, photoset_title=None):
    # create photoset
    if photoset_title:
        photoset, created = Photoset.objects.get_or_create(title=photoset_title, description='none')

    # get a list of photos
    photos = [os.path.join(photopath, f) for f in os.listdir(photopath) if os.path.isfile(os.path.join(photopath, f))]

    # set order counter
    order_counter = 0

    # upload all photos in folder and add them to database
    for photo in photos:

        # upload photo
        uploaded_photo = cloudinary.uploader.upload(photo)
        print('Photo uploaded. ID: %s' % uploaded_photo['public_id'])

        # save info in Photo table
        photo_db_instance = Photo.objects.create(publicID=uploaded_photo['public_id'], url=uploaded_photo['secure_url'])

        # add photo to photoset
        ps = PhotoInPhotoset(photoset=photoset, photo=photo_db_instance, order=order_counter)
        ps.save()
        order_counter += 1

    print('populate.py completed!')
    return


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: populate.py photoset_name')
        exit(1)
    else:
        print('Starting populate.py...')
        populate(photopath, sys.argv[1])
