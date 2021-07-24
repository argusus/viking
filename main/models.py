from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class ServiceManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().all()


class ServicesAndPrice(models.Model):
    service = models.CharField('Услуга RU', max_length=200)
    serviceUA = models.CharField('Послуга UA', max_length=200, null=True, blank=True)
    description = models.TextField('Описание RU', null=True, blank=True)
    descriptionUA = models.TextField('Опис UA', null=True, blank=True)
    price = models.DecimalField(_('Ціна'), max_digits=6, decimal_places=0)
    si = models.CharField('Единици измерения RU', max_length=20, null=True, blank=True, default='грн')
    siUA = models.CharField('Одиниці виміру UA', max_length=20, null=True, blank=True, default='грн')
    image = models.ImageField(_('Зображення'), null=True, blank=True, upload_to='var/www/file_project/media/images/')

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('service_detail', args=[str(self.id)])

    class Meta:
        verbose_name = _('Послуга')
        verbose_name_plural = _('Послуги')

    def __str__(self):
        return self.service

    objects = models.Manager()          # Менеджер за замовчуванням
    published = ServiceManager()        # Наш новий менеджер


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
