from django.db import models
from django_mysql.models import JSONField, Model


class Institute(models.Model):
    i_name = models.CharField(max_length=30);
    i_campus = models.CharField(max_length=15);
    class Meta:
        models.Index(fields=['i_name','i_campus','pk'])
        db_table = 'institutes'
    def __str__(self):
        return self.i_name+' - '+self.i_campus