from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from currency.models import ContactUs, Source


@admin.register(ContactUs)
class ContactUsAdmin(ImportExportModelAdmin):
    list_display = (
        'id',
        'email_from',
        'subject',
        'message',
    )
    search_fields = (
        'email_from',
        'subject',
        'message',
    )

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Source)
class SourceAdmin(ImportExportModelAdmin):
    list_display = (
        'id',
        'source_url',
        'name',
    )
    list_filter = (
        'name',
    )
    search_fields = (
        'source_url',
        'name',
    )
