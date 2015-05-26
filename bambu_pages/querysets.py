from django.db import models

class PageQuerySet(models.query.QuerySet):
    def root(self):
        return self.filter(parent__isnull = True)
