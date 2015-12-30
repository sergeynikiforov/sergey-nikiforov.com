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

# for exif
import exifread
import pytz
from datetime import datetime


# path to dir containing photos
PHOTOPATH = '/home/sergeynikiforov/Dropbox/assets_sn.com/my-site-final-images/photosets/spain/'

def dateTimeFromExif(path_to_file):
    """
    helper function
    expects path to photo with EXIF data

    returns datetime.datetime object from EXIF DateTimeOriginal field
    """
    with open(path_to_file, 'rb') as f:
        moscow_time = pytz.timezone('Europe/Moscow')
        tags = exifread.process_file(f, details=False)
        # try DateTimeOriginal if taken with digicam, otherwise - DateTimeDigitized (i.e. scanned film)
        try:
            dateTimeOriginal = tags['EXIF DateTimeOriginal'].values
        except KeyError:
            dateTimeOriginal = tags['EXIF DateTimeDigitized'].values
        dateTimeObject = datetime.strptime(dateTimeOriginal, '%Y:%m:%d %H:%M:%S')
        dateTimeObject = dateTimeObject.replace(tzinfo=moscow_time)
        return dateTimeObject


def populate(photos_path, photoset_title=None):
    """
    initial population of photoset

    #TODO - set 'date_taken' for Photo from EXIF using exifread
          - set 'thumbnail_url'
    """

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

        photo_datetime = dateTimeFromExif(photo)
        photo_thumb = cloudinary.CloudinaryImage(uploaded_photo['public_id']).build_url(secure=True, width=640, crop='fit')

        # save info in Photo table
        photo_db_instance = Photo.objects.create(publicID=uploaded_photo['public_id'], url=uploaded_photo['secure_url'], date_taken=photo_datetime, thumbnail_url=photo_thumb)

        # add photo to photoset
        ps = PhotoInPhotoset(photoset=photoset, photo=photo_db_instance, order=order_counter)
        ps.save()

        # increment counters
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
