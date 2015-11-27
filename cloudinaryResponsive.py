import sys
from django.utils.html import format_html
from django.utils.safestring import mark_safe
import cloudinary

def pictureElement(publicID, sizes, srcset, alt):
    """
    constructs HTML5 <picture> element with passed
    sizes, srcset and alt parameters from Cloudinary publicID image

    typical form of the returned result:
        <picture>
            <source
                sizes="(min-width: 640px) 60vw, 100vw"
                srcset="opera-200.webp 200w, ..."
                type="image/webp">
            <img
                src="opera-400.jpg" alt="The Oslo Opera House"
                sizes="(min-width: 640px) 60vw, 100vw"
                srcset="opera-200.jpg 200w, ...">
        </picture>

    sizes: string of valid sizes attribute
    srcset: tuple of strings - valid width parameters
    alt: string for <img alt="...">
    """
    srcsetWebp = ''
    srcsetJpg = ''
    sourceElement = ''
    imgElement = ''

    # construct srcset for Webp & jpeg images
    for src in srcset:
        width = int(src[:-1])
        srcsetWebp += '{photo_url} {src_width}, '.format(photo_url=cloudinary.CloudinaryImage(publicID).build_url(format="webp", width=width, crop="fill", quality=85), src_width=src)
        srcsetJpg += '{photo_url} {src_width}, '.format(photo_url=cloudinary.CloudinaryImage(publicID).build_url(format="jpg", width=width, crop="fill", quality=85), src_width=src)

    # remove trailing commas
    srcsetWebp = srcsetWebp[:-2]
    srcsetJpg = srcsetJpg[:-2]

    # construct <source> element
    sourceElement = format_html('<source sizes="{}" srcset="{}" type="image/webp">', mark_safe(sizes), mark_safe(srcsetWebp))

    # construct <img> element
    imgSrc = cloudinary.CloudinaryImage(publicID).build_url(format="jpg", width=1024, crop="fill")
    imgElement = format_html('<img id="{}" src="{}" alt="{}" sizes="{}" srcset="{}">', mark_safe(publicID), mark_safe(imgSrc), alt, mark_safe(sizes), mark_safe(srcsetJpg))

    return format_html('<picture> {} {} </picture>', mark_safe(sourceElement), mark_safe(imgElement))


def main():
    from cloudinaryconfig import cloud_name, api_key, api_secret
    cloudinary.config(
      cloud_name = cloud_name,
      api_key = api_key,
      api_secret = api_secret,
      cdn_subdomain = True,
      secure = True
    )
    print 'Sample output:'
    print pictureElement('123asd',"(min-width: 640px) 60vw, 100vw",('200w', '400w'),'opera house')
    return 0

if __name__=='__main__':
    sys.exit(main())