import sys
from django.utils.html import format_html
from django.utils.safestring import mark_safe
import cloudinary

def pictureElement(publicID, sizes, srcset, alt, portrait=False):
    """
    constructs HTML5 <picture> element with passed
    sizes, srcset and alt parameters from Cloudinary publicID image
    if portrait is True - it renders square photos

    https://dev.opera.com/articles/responsive-images/

    typical form of the returned result:
        <picture>
            <source
                media = "(orientation: portrait)"
                sizes="(min-width: 640px) 60vw, 100vw"
                srcset="opera-200-1x1.webp 200w, ..."
                type="image/webp">
            <source
                sizes="(min-width: 640px) 60vw, 100vw"
                srcset="opera-200.webp 200w, ..."
                type="image/webp">
            <source
                media = "(orientation: portrait)"
                sizes="(min-width: 640px) 60vw, 100vw"
                srcset="opera-200-1x1.jpg 200w, ...">
            <img
                src="opera-400.jpg" alt="The Oslo Opera House"
                sizes="(min-width: 640px) 60vw, 100vw"
                srcset="opera-200.jpg 200w, ...">
        </picture>

    sizes: string of valid sizes attribute
    srcset: list of strings - valid width parameters
    alt: string for <img alt="...">
    """
    srcsetWebp = ''
    srcsetJpg = ''
    sourceElement = ''
    imgElement = ''

    # construct srcset for Webp & jpeg images
    for src in srcset:
        width = int(src[:-1])
        srcsetWebp += '{photo_url} {src_width}, '.format(photo_url=cloudinary.CloudinaryImage(publicID).build_url(format="webp", width=width, crop="fill", quality=80), src_width=src)
        srcsetJpg += '{photo_url} {src_width}, '.format(photo_url=cloudinary.CloudinaryImage(publicID).build_url(format="jpg", width=width, crop="fill", quality=80), src_width=src)

    # remove trailing commas
    srcsetWebp = srcsetWebp[:-2]
    srcsetJpg = srcsetJpg[:-2]

    # construct <source> element
    sourceElement = format_html('<source sizes="{}" srcset="{}" type="image/webp">', mark_safe(sizes), mark_safe(srcsetWebp))

    # construct <img> element
    imgSrc = cloudinary.CloudinaryImage(publicID).build_url(format="jpg", width=1024, crop="fill")
    imgElement = format_html('<img src="{}" alt="{}" sizes="{}" srcset="{}">', mark_safe(imgSrc), alt, mark_safe(sizes), mark_safe(srcsetJpg))

    # if 'portrait' is checked
    if portrait:
        srcsetSquareWebp = ''
        srcsetSquareJpg = ''

        # construct srcset for Webp & jpeg images
        for src in srcset:
            width = int(src[:-1])
            srcsetSquareWebp += '{photo_url} {src_width}, '.format(photo_url=cloudinary.CloudinaryImage(publicID).build_url(format="webp", width=width, height=width, crop="fill", quality=80), src_width=src)
            srcsetSquareJpg += '{photo_url} {src_width}, '.format(photo_url=cloudinary.CloudinaryImage(publicID).build_url(format="jpg", width=width, height=width, crop="fill", quality=80), src_width=src)

        # remove trailing commas
        srcsetSquareWebp = srcsetSquareWebp[:-2]
        srcsetSquareJpg = srcsetSquareJpg[:-2]

        sourceSquareWebpElement = format_html('<source media="(orientation: portrait)" sizes="{}" srcset="{}" type="image/webp">', mark_safe(sizes), mark_safe(srcsetSquareWebp))

        sourceSquareJpgElement = format_html('<source media="(orientation: portrait)" sizes="{}" srcset="{}">', mark_safe(sizes), mark_safe(srcsetSquareJpg))

        return format_html('<picture> \n {sourcePortraitWebp} \n {source} \n {sourcePortraitJpg} \n {img} \n </picture>', sourcePortraitWebp=mark_safe(sourceSquareWebpElement), source=mark_safe(sourceElement), sourcePortraitJpg=mark_safe(sourceSquareJpgElement), img=mark_safe(imgElement))

    else:
        return format_html('<picture> \n {source} \n {img} \n </picture>', source=mark_safe(sourceElement), img=mark_safe(imgElement))


def main():
    from config import cloud_name, api_key, api_secret
    cloudinary.config(
      cloud_name = cloud_name,
      api_key = api_key,
      api_secret = api_secret,
      cdn_subdomain = True,
      secure = True
    )
    print 'Sample output:'
    print pictureElement('123asd',"(min-width: 640px) 60vw, 100vw",('200w', '400w'),'opera house', portrait=True)
    return 0

if __name__=='__main__':
    sys.exit(main())
