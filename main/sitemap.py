from django.contrib.sitemaps import Sitemap
from .models import ServicesAndPrice
from django.urls import reverse


class HomeSitemap(Sitemap):
    changefreq = 'never'
    priority = 0.9
    i18n = True

    def items(self):
        return ['home']

    def location(self, item):
        return reverse(item)


class AboutSitemap(Sitemap):
    changefreq = 'never'
    priority = 0.8
    i18n = True

    def items(self):
        return ['about', 'services']

    def location(self, item):
        return reverse(item)


class EntrySitemap(Sitemap):
    changefreq = 'never'
    priority = 0.4
    i18n = True

    def items(self):
        return ['create', 'order']

    def location(self, item):
        return reverse(item)


class ServiceAndPriceSitemap(Sitemap):
    changefreq = 'always'
    priority = 0.7
    i18n = True

    def items(self):
        return ServicesAndPrice.published.all()
