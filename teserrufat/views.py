from django.contrib import messages
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse, translate_url
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from teserrufat.models import (Service, DetailSidebar, FrequentlyAskedQuestions, AboutModel,
                               ContactImage,IndexVideo, OurWorks, IndexConfig, IndexSlider, Product, Partner)
from django.utils.translation import gettext_lazy as _
from django.db.models import Q

from teserrufat.forms import ContactForm


def set_language(request, lang_code):
    referer = request.META.get("HTTP_REFERER")

    if referer:
        response = redirect(translate_url(referer, lang_code))
    else:
        response = redirect(reverse('index'))

    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
    return response


def home_view(request):
    about = AboutModel.objects.first()
    index_config = IndexConfig.objects.first()
    index_slider = IndexSlider.objects.order_by("-created_at")
    video_part = IndexVideo.objects.first()
    services = Service.objects.order_by("-created_at")[:6]
    # services_total = Service.objects.order_by("-created_at")
    keyword = request.GET.get("service")
    partners = Partner.objects.order_by("-created_at")



    context = {
        "services": services,
        "about": about,
        "video_part": video_part,
        "keyword": keyword,
        "index_slider": index_slider,
        "index_config": index_config,
        "partners": partners,
    }
    return render(request, "index.html", context)


def about_view(request):
    about = AboutModel.objects.first()
    questions = FrequentlyAskedQuestions.objects.order_by("-created_at")

    # services_total = Service.objects.order_by("-created_at")
    # keyword = request.GET.get("service")
    #
    # if keyword:
    #     services_total = services_total.filter(Q(head_1__icontains=keyword),
    #                                            Q(head_2__icontains=keyword),
    #                                            Q(desc_1__icontains=keyword),
    #                                            Q(desc_2__icontains=keyword)
    #                                            )

    context = {
        "questions": questions,
        "about": about,
        # "services_total": services_total,
    }
    return render(request, "about.html", context)


def services_view(request):
    services = Service.objects.order_by("-created_at")

    keyword = request.GET.get("service")

    if keyword:
        services = services.filter(Q(head_1__icontains=keyword) |
                                   Q(head_1_ru__icontains=keyword) |
                                   Q(head_2__icontains=keyword) |
                                   Q(head_2_ru__icontains=keyword) |
                                   Q(desc_1__icontains=keyword) |
                                   Q(desc_1_ru__icontains=keyword) |
                                   Q(desc_2__icontains=keyword) |
                                   Q(desc_2_ru__icontains=keyword)
                                   )
    if request.GET.get("cat"):
        services = services.filter(category__name__icontains=request.GET.get("cat"))

    paginator = Paginator(services, 9)
    page = request.GET.get('page', 1)
    p = paginator.get_page(page)

    try:
        p = paginator.page(page)
    except PageNotAnInteger:
        p = paginator.page(1)
    except EmptyPage:
        p = paginator.page(paginator.num_pages)
    context = {
        "services": services,
        "p": p,
        "keyword": keyword,
        "cat": request.GET.get("cat"),

    }

    return render(request, "services.html", context)


def contact_view(request):
    form = ContactForm()
    photo = ContactImage.objects.first()

    # services_total = Service.objects.order_by("-created_at")
    # keyword = request.GET.get("service")
    #
    # if keyword:
    #     services_total = services_total.filter(Q(head_1__icontains=keyword),
    #                                            Q(head_2__icontains=keyword),
    #                                            Q(desc_1__icontains=keyword),
    #                                            Q(desc_2__icontains=keyword)
    #                                            )

    if request.method == "POST":
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, _("Məlumatlar göndərildi"))

            form = ContactForm()
        else:
            messages.error(request, _("Problem yaşandı.."))
    context = {
        "form": form,
        # "services_total": services_total,
        "photo": photo,
    }
    return render(request, "contact.html", context)


def our_works(request):
    ourWorks = OurWorks.objects.order_by("-created_at")

    # services_total = Service.objects.order_by("-created_at")
    # keyword = request.GET.get("service")
    #
    # if keyword:
    #     services_total = services_total.filter(Q(head_1__icontains=keyword),
    #
    #                                            Q(head_2__icontains=keyword),
    #
    #                                            Q(desc_1__icontains=keyword),
    #
    #                                            Q(desc_2__icontains=keyword),
    #
    #                                            )

    paginator = Paginator(ourWorks, 6)
    page = request.GET.get('page', 1)
    p = paginator.get_page(page)

    try:
        p = paginator.page(page)
    except PageNotAnInteger:
        p = paginator.page(1)
    except EmptyPage:
        p = paginator.page(paginator.num_pages)
    context = {
        "our_works": ourWorks,
        "p": p,
        # "services_total": services_total,

    }

    return render(request, "ourworks.html", context)



def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    sidebar = DetailSidebar.objects.first()
    context = {

        "service": service,
        "sidebar":sidebar,


    }
    return render(request, "service-details.html", context)


def products_view(request):
    products = Product.objects.order_by("-created_at")

    if request.GET.get("cat"):
        products = products.filter(category__name__icontains=request.GET.get("cat"))

    paginator = Paginator(products, 9)
    page = request.GET.get('page', 1)
    p = paginator.get_page(page)

    try:
        p = paginator.page(page)
    except PageNotAnInteger:
        p = paginator.page(1)
    except EmptyPage:
        p = paginator.page(paginator.num_pages)
    context = {
        "products": products,
        "p": p,
        "cat": request.GET.get("cat"),

    }

    return render(request, "products.html", context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {

        "product": product,

    }
    return render(request, "product-details.html", context)