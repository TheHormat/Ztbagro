from django import forms
from teserrufat.models import Contact
from django.utils.translation import gettext_lazy as _

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ("created_at", "updated_at", "slug")

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].required = True
            self.fields[field].widget.attrs.update({"class": "form-control"})

        self.fields['full_name'].widget.attrs.update({"type": "text", "placeholder": _("Ad və soyadınız"), "id": "name"})
        self.fields['phone_number'].widget.attrs.update({"type":"text", "placeholder": _("Əlaqə nömrəsi"), "id": "phone"})
        self.fields['email'].widget.attrs.update({"type": "email", "placeholder": _("E-poçt ünvanınız"), "id": "email"})
        self.fields['message'].widget.attrs.update({"rows": 4, "placeholder": _("Mesajınız"), "id": "message"})

    def clean_phone_number(self):
        phone = self.cleaned_data.get("phone_number")
        for elem in phone:
            if elem.isalpha():
                raise forms.ValidationError(_("Telefon nömrəsində yalnışlıq var.."))
        return phone
