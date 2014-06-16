from __future__ import unicode_literals

from django.db import models

from .choices import PublishChoice, VisibilityChoice


class VisibleQueryset(models.query.QuerySet):

    def public(self):
        return self.filter(visibility=VisibilityChoice.Public)

    def private(self):
        return self.filter(visibility=VisibilityChoice.Private)


class AuthorableQueryset(models.query.QuerySet):

    def author(self, user):
        return self.filter(created_by__username=user)


class PublishableQueryset(models.query.QuerySet):

    def published(self):
        return self.filter(publish_state=PublishChoice.Published)

    def unpublished(self):
        return self.filter().exclude(publish_state=PublishChoice.Published)
