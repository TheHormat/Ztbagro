from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from services.mixin import DateMixin, SlugMixin
from services.generator import Generator
from services.uploader import Uploader
from services.extract import extract_yt_video_url_from_iframe
from services.choices import SOCIAL_CHOICES, PAGE_CHOICES


class Category(DateMixin, SlugMixin):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Kateqoriya"
        verbose_name_plural = "Kateqoriyalar"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=Category)
        super(Category, self).save(*args, **kwargs)


class Service(DateMixin, SlugMixin):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    main_image = models.ImageField(upload_to=Uploader.upload_photo_for_service, verbose_name="Esas sekil",
                                   help_text="720x584")
    head_1 = models.CharField(max_length=255, verbose_name="Basliq 1", null=True, blank=True)
    desc_1 = RichTextField(null=True, blank=True)
    head_2 = models.CharField(max_length=255, verbose_name="Basliq 2", null=True, blank=True)
    desc_2 = RichTextField(null=True, blank=True)

    page_title = models.CharField(max_length=300, null=True, blank=True, verbose_name="Sehifenin title i")
    page_description = models.TextField(null=True, blank=True, verbose_name="Sehifenin descriptionu")

    def __str__(self):
        return self.head_1

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Xidmət"
        verbose_name_plural = "Xidmətlər"

    def get_absolute_url(self):
        return reverse("service_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=Service)
        super(Service, self).save(*args, **kwargs)


class ServiceImages(DateMixin, SlugMixin):
    images = models.ImageField(upload_to=Uploader.upload_photo_for_service)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Xidmət şəkili"
        verbose_name_plural = "Xidmətlərin şəkilləri"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=ServiceImages)
        super(ServiceImages, self).save(*args, **kwargs)


class ServiceQualities(DateMixin, SlugMixin):
    name = models.CharField(max_length=255, verbose_name="Keyfiyyətlər")
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Keyfiyyət"
        verbose_name_plural = "Keyfiyyətlər"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=ServiceQualities)
        super(ServiceQualities, self).save(*args, **kwargs)


class FrequentlyAskedQuestions(DateMixin, SlugMixin):
    question = models.CharField(max_length=255, verbose_name="Sual")
    answer = RichTextField(verbose_name="Cavab")

    def __str__(self):
        return self.question

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Tez-tez verilən sual"
        verbose_name_plural = "Tez-tez verilən suallar"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=FrequentlyAskedQuestions)
        super(FrequentlyAskedQuestions, self).save(*args, **kwargs)


class AboutModel(DateMixin, SlugMixin):
    main_image = models.ImageField(upload_to=Uploader.upload_photo_for_about, verbose_name="Əsas şəkil",
                                   help_text="500x645")
    head = models.CharField(max_length=255, verbose_name="Başlıq")
    description = RichTextField(verbose_name="Açıqlama")
    left_image = models.ImageField(upload_to=Uploader.upload_photo_for_about, verbose_name="Sol şəkil",
                                   help_text="300x400")
    right_top_image = models.ImageField(upload_to=Uploader.upload_photo_for_about, verbose_name="Yuxarı sağ şəkil",
                                        help_text="300x280")
    right_bottom_image = models.ImageField(upload_to=Uploader.upload_photo_for_about, verbose_name="Aşağı sağ şəkil",
                                           help_text="300x280")

    def __str__(self):
        return self.head

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Haqqımızda"
        verbose_name_plural = "Haqqımızda"

    def save(self, *args, **kwargs):

        if not self.id and AboutModel.objects.exists():

            myobj = AboutModel.objects.first()
            myobj.head = self.head
            myobj.description = self.description
            myobj.main_image = self.main_image
            myobj.left_image = self.left_image
            myobj.right_top_image = self.right_top_image
            myobj.right_bottom_image = self.right_bottom_image
            myobj.save()
        else:
            if not self.slug:
                self.slug = Generator.create_slug_shortcode(size=15, model_=AboutModel)
            super(AboutModel, self).save(*args, **kwargs)


class Contact(DateMixin, SlugMixin):
    full_name = models.CharField(max_length=255, verbose_name="Ad və soyad")
    phone_number = models.CharField(max_length=255, verbose_name="Əlaqə nömrəsi")
    email = models.EmailField(max_length=255, verbose_name="E-poçt ünvanı")
    message = models.TextField(verbose_name="Mesaj")

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Əlaqə saxlamaq istəyən şəxs"
        verbose_name_plural = "Əlaqə saxlamaq istəyən şəxslər"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=Contact)
        super(Contact, self).save(*args, **kwargs)


class OurWorks(DateMixin, SlugMixin):
    iframe_link = models.TextField(verbose_name="Video linki")

    def __str__(self):
        return self.iframe_link

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Bizim iş"
        verbose_name_plural = "Bizim işlərimiz"

    def save(self, *args, **kwargs):
        extracted_url = extract_yt_video_url_from_iframe(self.iframe_link)
        if extracted_url:
            self.iframe_link = extracted_url
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=OurWorks)

        extracted_url = extract_yt_video_url_from_iframe(self.iframe_link)
        if extracted_url:
            self.iframe_link = extracted_url

        super(OurWorks, self).save(*args, **kwargs)


class IndexVideo(DateMixin, SlugMixin):
    video_url = models.TextField(verbose_name="Video linki", null=True, blank=True)
    video_cover_img = models.ImageField(upload_to=Uploader.upload_video_for_index, verbose_name="Video örtük şəkili",
                                        null=True, blank=True)
    word = models.CharField(max_length=255, null=True, blank=True, verbose_name="Video üzərindəki yazı")

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Ana səhifə video"
        verbose_name_plural = "Ana səhifə video"

    def save(self, *args, **kwargs):

        if not self.id and IndexVideo.objects.exists():

            myobj = IndexVideo.objects.first()
            myobj.video_url = self.video_url
            myobj.video_cover_img = self.video_cover_img
            myobj.word = self.word

            myobj.save()
        else:
            if not self.slug:
                self.slug = Generator.create_slug_shortcode(size=15, model_=IndexVideo)

            super(IndexVideo, self).save(*args, **kwargs)


class IndexConfig(DateMixin, SlugMixin):
    header_logo = models.ImageField(upload_to=Uploader.upload_logo_for_index, verbose_name="Yuxarı loqo")
    footer_logo = models.ImageField(upload_to=Uploader.upload_logo_for_index, verbose_name="Aşağı loqo")
    footer_text = RichTextField(verbose_name="Footer mətn")
    keywords = models.TextField(verbose_name="Keywordler", help_text="vergul ile ayrilmis sekilde yazilsin", null=True, blank=True)
    favicon = models.ImageField(upload_to=Uploader.upload_image_for_favicon, verbose_name="Favikon", null=True,
                                blank=True)

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Əsas məlumat"
        verbose_name_plural = "Əsas məlumatlar"

    def save(self, *args, **kwargs):

        if not self.id and IndexConfig.objects.exists():

            myobj = IndexConfig.objects.first()
            myobj.header_logo = self.header_logo
            myobj.footer_logo = self.footer_logo
            myobj.footer_text = self.footer_text
            myobj.favicon = self.favicon

            myobj.save()
        else:
            if not self.slug:
                self.slug = Generator.create_slug_shortcode(size=15, model_=IndexConfig)

            super(IndexConfig, self).save(*args, **kwargs)


class IndexSlider(DateMixin, SlugMixin):
    images = models.ImageField(upload_to=Uploader.upload_slider_image_for_index,
                               verbose_name="Ana səhifə slider şəkilləri")
    head_1 = models.CharField(max_length=255, verbose_name="Şəkilin üzərindəki rəngli yazı")
    main_sentence = models.CharField(max_length=255, verbose_name="Əsas böyük yazı")
    little_sentence = models.CharField(max_length=255, verbose_name="Şrifti kiçik olan yazı")

    def __str__(self):
        return self.head_1

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Ana səhifə slider parametr"
        verbose_name_plural = "Ana səhifə slider parametrləri"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=IndexSlider)
        super(IndexSlider, self).save(*args, **kwargs)


class DetailSidebar(DateMixin, SlugMixin):
    top_sentence = models.CharField(max_length=255, verbose_name="Yuxarıdakı cümlə", null=True, blank=True)
    bottom_sentence = models.CharField(max_length=255, verbose_name="Aşağıdakı cümlə", null=True, blank=True)

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Detal səhifəsi yan hissə"
        verbose_name_plural = "Detal səhifəsi yan hissə"

    def save(self, *args, **kwargs):

        if not self.id and DetailSidebar.objects.exists():

            myobj = DetailSidebar.objects.first()

            myobj.top_sentence = self.top_sentence
            myobj.bottom_sentence = self.bottom_sentence

            myobj.save()
        else:
            if not self.slug:
                self.slug = Generator.create_slug_shortcode(size=15, model_=DetailSidebar)

            super(DetailSidebar, self).save(*args, **kwargs)


class ContactImage(DateMixin, SlugMixin):
    image = models.ImageField(upload_to=Uploader.upload_image_for_sidebar, help_text="456x516")

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Əlaqə formunun yanındakı şəkil"
        verbose_name_plural = "Əlaqə formunun yanındakı şəkil"

    def save(self, *args, **kwargs):

        if not self.id and ContactImage.objects.exists():

            myobj = ContactImage.objects.first()

            myobj.image = self.image

            myobj.save()
        else:
            if not self.slug:
                self.slug = Generator.create_slug_shortcode(size=15, model_=ContactImage)

            super(ContactImage, self).save(*args, **kwargs)


class Phones(DateMixin, SlugMixin):
    main_data = models.ForeignKey(IndexConfig, on_delete=models.SET_NULL, null=True, blank=True)
    phones = models.CharField(max_length=255, verbose_name="Əlaqə nömrəsi")
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.phones

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Əlaqə nömrəsi"
        verbose_name_plural = "Əlaqə nömrələri"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=Phones)
        super(Phones, self).save(*args, **kwargs)


class Emails(DateMixin, SlugMixin):
    main_data = models.ForeignKey(IndexConfig, on_delete=models.SET_NULL, null=True, blank=True)
    emails = models.EmailField(verbose_name="Email")
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.emails

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Email"
        verbose_name_plural = "Emaillər"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=Emails)
        super(Emails, self).save(*args, **kwargs)


class Address(DateMixin, SlugMixin):
    main_data = models.ForeignKey(IndexConfig, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.TextField(verbose_name="Ünvan")
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.address

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "Ünvan"
        verbose_name_plural = "Ünvanlar"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=Address)
        super(Address, self).save(*args, **kwargs)


class SocialMedia(DateMixin, SlugMixin):
    social_type = models.CharField(max_length=255, choices=SOCIAL_CHOICES, verbose_name="Sosial media")
    social_link = models.TextField(verbose_name="Sosial media linki")

    def __str__(self):
        return self.social_type

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "Sosial media"
        verbose_name_plural = "Sosial media hesabları"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=SocialMedia)
        super(SocialMedia, self).save(*args, **kwargs)


class TitleDescription(DateMixin, SlugMixin):
    page_type = models.CharField(max_length=255, choices=PAGE_CHOICES, verbose_name="Səhifənin tipi")
    page_title = models.CharField(max_length=255, verbose_name="Səhifənın başlığı")
    page_slide_image = models.ImageField(upload_to=Uploader.upload_image_for_pages_slider, verbose_name="Səhifə yuxarı hissə şəkil", help_text="2038x549", null=True, blank=True)
    page_description = models.TextField(verbose_name="Səhifənin açıqlaması")


    def __str__(self):
        return self.page_title

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "Başlıq"
        verbose_name_plural = "Başlıqlar"


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=TitleDescription)
        super(TitleDescription, self).save(*args, **kwargs)

class Subscribe(DateMixin, SlugMixin):
    email = models.EmailField(verbose_name="E-poçt ünvanı")

    def __str__(self):
        return self.email

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Abunə"
        verbose_name_plural = "Abunələr"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=Subscribe)
        super(Subscribe, self).save(*args, **kwargs)


class ProductCategory(DateMixin, SlugMixin):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Məhsul kateqoriyası"
        verbose_name_plural = "Məhsul kateqoriyaları"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=ProductCategory)
        super(ProductCategory, self).save(*args, **kwargs)


class Product(DateMixin, SlugMixin):
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True, blank=True)
    main_image = models.ImageField(upload_to=Uploader.upload_photo_for_product, verbose_name="Əsas şəkil")
    title = models.CharField(max_length=255, verbose_name="Başlıq")
    subtitle = models.CharField(max_length=255, null=True, blank=True, verbose_name="Alt başlıq")
    short_description = models.TextField(null=True, blank=True, verbose_name="Qısa açıqlama")

    head_1 = models.CharField(max_length=255, null=True, blank=True, verbose_name="Başlıq 1")
    desc_1 = RichTextField(null=True, blank=True, verbose_name="Açıqlama 1")
    head_2 = models.CharField(max_length=255, null=True, blank=True, verbose_name="Başlıq 2")
    desc_2 = RichTextField(null=True, blank=True, verbose_name="Açıqlama 2")

    page_title = models.CharField(max_length=300, null=True, blank=True, verbose_name="Sehifenin title i")
    page_description = models.TextField(null=True, blank=True, verbose_name="Sehifenin descriptionu")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Məhsul"
        verbose_name_plural = "Məhsullar"

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=Product)
        super(Product, self).save(*args, **kwargs)


class ProductDocument(DateMixin, SlugMixin):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, verbose_name="Sənədin adı")
    file = models.FileField(upload_to=Uploader.upload_document_for_product, verbose_name="Sənəd")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Məhsul sənədi"
        verbose_name_plural = "Məhsul sənədləri"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=ProductDocument)
        super(ProductDocument, self).save(*args, **kwargs)


class ProductTable(DateMixin, SlugMixin):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255, verbose_name="Cədvəlin başlığı")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Məhsul cədvəli"
        verbose_name_plural = "Məhsul cədvəlləri"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=ProductTable)
        super(ProductTable, self).save(*args, **kwargs)


class ProductTableRow(DateMixin, SlugMixin):
    table = models.ForeignKey(ProductTable, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, verbose_name="Ad")
    value = models.CharField(max_length=255, verbose_name="Dəyər")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Cədvəl sətri"
        verbose_name_plural = "Cədvəl sətirləri"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=ProductTableRow)
        super(ProductTableRow, self).save(*args, **kwargs)


class Partner(DateMixin, SlugMixin):
    image = models.ImageField(upload_to=Uploader.upload_logo_for_partner, verbose_name="Loqo")
    link = models.URLField(max_length=500, null=True, blank=True, verbose_name="Link")

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Partnyor"
        verbose_name_plural = "Partnyorlar"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=Partner)
        super(Partner, self).save(*args, **kwargs)

