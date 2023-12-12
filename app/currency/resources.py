from import_export import resources

from currency.models import ContactUs, Source


class ContactUsResource(resources.ModelResource):

    class Meta:
        model = ContactUs


class SourceResource(resources.ModelResource):

    class Meta:
        model = Source
