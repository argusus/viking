from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class ServicesAndPrice(models.Model):
    service = models.CharField(_('Послуга'), max_length=100)
    serviceUA = models.CharField(_('Послуга UA'), max_length=100, null=True, blank=True)
    description = models.TextField(_('Опис'), null=True, blank=True)
    descriptionUA = models.TextField(_('Опис UA'), null=True, blank=True)
    price = models.DecimalField(_('Ціна'), max_digits=6, decimal_places=0)
    si = models.CharField(_('Одиниці виміру'), max_length=20, null=True, blank=True, default='грн')
    siUA = models.CharField(_('Одиниці виміру UA'), max_length=20, null=True, blank=True, default='грн')
    image = models.ImageField(_('Зображення'), null=True, blank=True, upload_to='var/www/file_project/media/images/')

    def __str__(self):
        return self.service

    class Meta:
        verbose_name = _('Послуга')
        verbose_name_plural = _('Послуги')


class Questions(models.Model):
    tel = models.CharField(_('Номер телефону'), max_length=13)
    name = models.CharField(_("Ім'я"), max_length=100)
    text_questions = models.TextField(_('Текст питання'))
    time_question = models.DateTimeField(_('Час створення'), default=timezone.now)

    def __str__(self):
        return self.tel

    class Meta:
        verbose_name = _('Питання')
        verbose_name_plural = _('Питання')


class OrderServices(models.Model):

    tel_service = models.CharField(_('Номер телефону'), max_length=13)
    name_service = models.CharField(_("Ім'я"), max_length=100)
    choice_service = models.CharField(_('Замовлення послуги'), max_length=200, null=True, blank=True)
    text_service = models.TextField(_('Побажання'), null=True, blank=True)
    time_service = models.DateTimeField(_('Час створення'), default=timezone.now)

    def __str__(self):
        return self.tel_service

    class Meta:
        verbose_name = _('Замовлення')
        verbose_name_plural = _('Замовлення')
