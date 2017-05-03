from django.db import models


class UserLink(models.Model):
    class Meta:
        db_table='form_set_userlink'

    user = models.CharField('User', max_length=200, null=True, blank=True)
    anchor = models.DateTimeField('Link', max_length=200, null=True, blank=True)
