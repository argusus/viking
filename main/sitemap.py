from django.contrib.sitemaps import Sitemap
from .models import ServicesAndPrice
from django.urls import reverse


class ServiceAndPriceSitemap(Sitemap):
    changefreq = 'always'
    priority = 0.8
    i18n = True

    def items(self):
        return ServicesAndPrice.published.all()

    # def lastmod(self, obj):
    #     return obj.id


# class StaticViewsSitemap(Sitemap):
#     # changefreq = 'daily'
#     priority = 0.9
#     i18n = True
#
#     def items(self):
#         return ['index', 'about', 'services']
#
#     def location(self, item):
#         return reverse(item)
