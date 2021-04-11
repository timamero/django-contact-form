# referenceS: 
# https://docs.djangoproject.com/en/3.1/topics/forms/
# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms

from django.forms import ModelForm

from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone', 'message']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs['placeholder'] = field.label
