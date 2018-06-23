from django.db import models
from django_mysql.models import JSONField, Model
import datetime
from django.conf import settings
from institutions.models import *

def json_posts_default():
    return dict
    # return {
    # "usertype":"",
    # "about":"",
    # "birthday":"",
    # "fav_book":"",
    # "fav_song":"",
    # "fav_movie":"",
    # "fav_quote":"",
    # "interest":"",
    # "joined":"",
    # "gender":"",
    # "religion":""
    # }
class UserInfo(models.Model):
    user_id = models.IntegerField(settings.AUTH_USER_MODEL, default=1, primary_key=True)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, default=1)
    #don't forget this query
    #check default before publishing
    j_user = JSONField(default=json_posts_default())
    class Meta:
        models.Index(fields=['user_id']),
        db_table = 'user_info'
    def __str__(self):
        return 'User : '+str(self.user_id)+' Posted : ' + str(self.institute)
class UserCount(models.Model):
    user_id = models.IntegerField(settings.AUTH_USER_MODEL, default=1, primary_key=True)
    no_liked = models.IntegerField(default=0)
    no_likes = models.IntegerField(default=0)
    no_comments = models.IntegerField(default=0)
    lastonline = models.DateField(auto_now_add=True)
    class Meta:
        models.Index(fields=['user_id'])
        db_table = 'user_counter'
    def __str__(self):
        return 'User : '+str(self.user_id)+' Last Online : ' + self.lastonline