from django.utils.text import slugify


def unique_slug_generator(slug,model_class,key=0):
    slugs = slug
    if key:
        slugs = slug + "-" + str(key)
    slugs = slugify(slugs)
    qs_exists = model_class.objects.filter(slug=slugs)
    if qs_exists.count():
        slugs = unique_slug_generator(slug,model_class,key+1)
    return slugs


def to_int(data):
    if data:
        try:
            return int(data)
        except Exception as e:
            print(e)
    return 0

