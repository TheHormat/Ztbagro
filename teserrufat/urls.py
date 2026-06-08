from django.urls import path
from teserrufat.views import *

urlpatterns = [


    path("", home_view, name='home'),
    path("about/", about_view, name='about'),
    path("services/", services_view, name='services'),
    path("contact/", contact_view, name='contact'),
    path("our-works/", our_works, name='our_works'),
    path("service/detail/<slug>/", service_detail, name="service_detail"),
    path("products/", products_view, name='products'),
    path("product/detail/<slug>/", product_detail, name="product_detail"),



    
]