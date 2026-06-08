from django.shortcuts import redirect

from teserrufat.models import Category, IndexConfig, TitleDescription, SocialMedia, Subscribe



def my_sender(request):
    categories = Category.objects.order_by("name")
    index_config = IndexConfig.objects.first()
    titles = TitleDescription.objects.all()
    social_media = SocialMedia.objects.all()
    sub = request.POST.get("sub")
    if sub:
        s = Subscribe.objects.create(
            email=sub
        )
        s.save()

    return {
            "categories": categories,
            "index_config": index_config,
            "titles": titles,
            "social_media": social_media,

            }
