from django.utils.translation import gettext_lazy as _


SOCIAL_CHOICES = (
    ("insta", "Instagram"),
    ("fb", "Facebook"),
    ("wp","WhatsApp"),
    ("twitter","Twitter"),
    ("linkedin", "Linkedin"),
    ("tiktok", "Tiktok"),
    ("yt", "YouTube"),
    ("telegram", "Telegram"),
)


PAGE_CHOICES = (
    ("home", _("Home Page")),
    ("about", _("About page")),
    ("contact", _("Contact")),
    ("services", _("Services")),
    ("our_works", _("Our Works")),
    ("service_detail", _("Service detail")),
)