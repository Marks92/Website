from __future__ import unicode_literals

from django.db import models


class ContactMessage(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email
