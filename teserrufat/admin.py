
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from teserrufat.models import (Service, ServiceImages, Category, ServiceQualities, FrequentlyAskedQuestions,
                               AboutModel,IndexVideo, OurWorks, Contact, IndexConfig,DetailSidebar, IndexSlider,
                               ContactImage, Phones, Emails, Address, TitleDescription, SocialMedia, Subscribe,
                               ProductCategory, Product, ProductDocument, ProductTable, ProductTableRow, Partner)


class ImageInLineService(admin.StackedInline):
    model = ServiceImages
    extra = 1

class QualitiesInline(TranslationTabularInline):
    model = ServiceQualities
    extra = 1



@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    inlines = [ImageInLineService, QualitiesInline]

    class Media:
        js = (

            'modeltranslation/js/tabbed_translation_fields.js',
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
        )

        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    class Media:
        js = (

            'modeltranslation/js/tabbed_translation_fields.js',
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
        )

        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(FrequentlyAskedQuestions)
class FrequentlyAskedQuestionsAdmin(TranslationAdmin):
    class Media:
        js = (

            'modeltranslation/js/tabbed_translation_fields.js',
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
        )

        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(AboutModel)
class AboutAdmin(TranslationAdmin):
    class Media:
        js = (

            'modeltranslation/js/tabbed_translation_fields.js',
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
        )

        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(IndexVideo)
class IndexVideoAdmin(TranslationAdmin):
    class Media:
        js = (

            'modeltranslation/js/tabbed_translation_fields.js',
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
        )

        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

class AddressAdmin(TranslationTabularInline):
    model = Address
    extra = 0
    class Media:
        js = (

            'modeltranslation/js/tabbed_translation_fields.js',
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
        )

        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

class PhonesAdmin(admin.TabularInline):
    model = Phones
    extra = 0
    class Media:
        js = (

            'modeltranslation/js/tabbed_translation_fields.js',
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
        )

        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

class EmailsAdmin(admin.TabularInline):
    model = Emails
    extra = 0
    class Media:
        js = (

            'modeltranslation/js/tabbed_translation_fields.js',
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
        )

        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(IndexConfig)
class IndexConfigAdmin(TranslationAdmin):
    inlines = [AddressAdmin, PhonesAdmin, EmailsAdmin]
    class Media:
        js = (

            'modeltranslation/js/tabbed_translation_fields.js',
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
        )

        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(TitleDescription)
class TitleDescriptionAdmin(TranslationAdmin):
    class Media:
        js = (

            'modeltranslation/js/tabbed_translation_fields.js',
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
        )

        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(IndexSlider)
class IndexSliderAdmin(TranslationAdmin):
    class Media:
        js = (

            'modeltranslation/js/tabbed_translation_fields.js',
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
        )

        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class DocumentInLineProduct(admin.StackedInline):
    model = ProductDocument
    extra = 1


class ProductTableRowInline(TranslationTabularInline):
    model = ProductTableRow
    extra = 1


@admin.register(ProductCategory)
class ProductCategoryAdmin(TranslationAdmin):
    class Media:
        js = (

            'modeltranslation/js/tabbed_translation_fields.js',
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
        )

        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    inlines = [DocumentInLineProduct]

    class Media:
        js = (

            'modeltranslation/js/tabbed_translation_fields.js',
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
        )

        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(ProductTable)
class ProductTableAdmin(TranslationAdmin):
    inlines = [ProductTableRowInline]

    class Media:
        js = (

            'modeltranslation/js/tabbed_translation_fields.js',
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
        )

        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    pass


admin.site.register(OurWorks)
admin.site.register(DetailSidebar)
admin.site.register(Contact)
admin.site.register(ContactImage)
admin.site.register(SocialMedia)
admin.site.register(Subscribe)

