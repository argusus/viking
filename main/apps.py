from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
    verbose_name = _('Структура і форми сайту')
