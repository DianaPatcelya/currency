from django import forms

from currency.models import Source, Rate, ContactUs


class RateForm(forms.ModelForm):

    class Meta:
        model = Rate
        fields = (
            'buy',
            'sell',
            'currency_type',
            'source',
        )


class SourceForm(forms.ModelForm):

    class Meta:
        model = Source
        fields = (
            'source_url',
            'name',
        )


class ContactUsForm(forms.ModelForm):

    class Meta:
        model = ContactUs
        fields = (
            'name',
            'email_from',
            'subject',
            'message'
        )
