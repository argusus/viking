from django.contrib.sitemaps import Sitemap
from .models import ServicesAndPrice
from django.urls import reverse


class ServiceAndPriceSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9
    i18n = True

    def items(self):
        return ServicesAndPrice.objects.all()

    def lastmod(self, obj):
        return obj.service


# class StaticViewsSitemap(Sitemap):
#     changefreq = 'daily'
#     priority = 1.0
#     i18n = True
#
#     def items(self):
#         return ['index', 'about', 'services']
#
#     def location(self, item):
#         return reverse(item)
