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
PHOTOPATH = '/home/sergeynikiforov/Dropbox/img_assets/test2/'

def populate(photos_path, photoset_title=None):
    # create photoset
    if photoset_title:
        photoset, created = Photoset.objects.get_or_create(title=photoset_title, description='none')

    # get a list of photos
    photos = [os.path.join(PHOTOPATH, f) for f in os.listdir(PHOTOPATH) if os.path.isfile(os.path.join(PHOTOPATH, f))]

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

        # increment counters
        photoset.num_photos += 1
        order_counter += 1

    # save changes to photoset
    photoset.save()
    print('populate.py completed!')
    return


def main():
    if len(sys.argv) != 2:
        sys.exit('usage: populate.py photoset_name')
    else:
        print('Starting populate.py...')
        populate(PHOTOPATH, sys.argv[1])
        return 0


if __name__ == '__main__':
    sys.exit(main())
