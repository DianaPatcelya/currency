from django.db import models
from django.utils.translation import gettext_lazy as _

from currency.choices import CurrencyTypeChoices


class Rate(models.Model):
    buy = models.DecimalField(_('Buy'), max_digits=6, decimal_places=2)
    sell = models.DecimalField(_('Sell'), max_digits=6, decimal_places=2)
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    currency_type = models.SmallIntegerField(
        _('Currency type'),
        choices=CurrencyTypeChoices.choices,
        default=CurrencyTypeChoices.USD
    )
    source = models.CharField(_('Source'), max_length=255)

    class Meta:
        verbose_name = _('Rate')
        verbose_name_plural = _('Rates')


class ContactUs(models.Model):
    email_from = models.EmailField(_('Email from'), )
    subject = models.CharField(_('Subject'), max_length=30)
    message = models.CharField(_('Message'), max_length=255)
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    name = models.CharField(_('Name'), max_length=64, default='Name')

    class Meta:
        verbose_name = _('Contact Us')
        verbose_name_plural = _('Contact Us')

    def __str__(self):
        return f'{self.email_from} - {self.subject}'


class Source(models.Model):
    source_url = models.URLField(_('Source url'), max_length=255)
    name = models.CharField(_('Name'), max_length=64)

    class Meta:
        verbose_name = _('Source')
        verbose_name_plural = _('Sources')

    def __str__(self):
        return f'{self.name}'


class RequestResponseLog(models.Model):
    path = models.CharField(max_length=255)
    REQUEST_METHOD_CHOICES = [('GET', 'GET'), ('POST', 'POST')]
    request_method = models.CharField(max_length=10, choices=REQUEST_METHOD_CHOICES)
    time = models.IntegerField()

    def __str__(self):
        return f"{self.path} - {self.request_method} {self.time}"
