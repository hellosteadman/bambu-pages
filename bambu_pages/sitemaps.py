from django.contrib.sitemaps import Sitemap
from bambu_pages.models import Page

class PageSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.5
    
    def items(self):
        return Page.objects.all()