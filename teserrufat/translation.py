from modeltranslation.translator import TranslationOptions, register
from teserrufat.models import (Service, Category, ServiceQualities, FrequentlyAskedQuestions, AboutModel, IndexConfig,
                               IndexVideo, IndexSlider, Address, TitleDescription)


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ("head_1", "desc_1", "head_2", "desc_2", "page_title", "page_description")


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(ServiceQualities)
class ServiceQualitiesTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(FrequentlyAskedQuestions)
class FrequentlyAskedTranslationOptions(TranslationOptions):
    fields = ("question", "answer",)


@register(AboutModel)
class AboutTranslationOptions(TranslationOptions):
    fields = ("head", "description")


@register(IndexConfig)
class IndexConfigTranslationOptions(TranslationOptions):
    fields = ("footer_text", "keywords")


@register(IndexVideo)
class IndexVideoTranslationOptions(TranslationOptions):
    fields = ("word",)


@register(IndexSlider)
class IndexSliderTranslationOptions(TranslationOptions):
    fields = ("head_1", "main_sentence", "little_sentence")

@register(Address)
class AddressTranslationOptions(TranslationOptions):
    fields = ("address", )

@register(TitleDescription)
class TitleDescriptionTranslationOptions(TranslationOptions):
    fields = ("page_title", "page_description")

