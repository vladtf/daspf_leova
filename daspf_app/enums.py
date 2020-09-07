from django.db import models
from django.utils.translation import gettext_lazy as _


class MessageStatus(models.TextChoices):
    NEW = 'N', _('Nou')
    SEEN = 'V', _('Văzut')
    RESPONDED = 'R', _('Răspuns')
    RESOLVED = 'S', _('Soluționat')
