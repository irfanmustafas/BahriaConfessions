from django.db import models
from django_mysql.models import JSONField, Model
import datetime
from django.conf import settings
from institutions.models import *

def json_posts_default():
#    return dict
    return {"cont": "Post","loc": "Islamabad","tags": " "}
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, default=1) #Adding on delete do nothing
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, default=1)
    posted_at = models.DateTimeField(auto_now_add=True,blank=False)
    jcont = JSONField(default=json_posts_default,blank=False)
    class Meta:
        models.Index(fields=['user_id','post_id','institute'])
        db_table = 'posts'
        ordering = ['-posted_at']
    def __str__(self):
        return  'User : '+str(self.user_id)+' Posted : ' + str(self.post_id)
