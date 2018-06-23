from __future__ import unicode_literals
from django.urls import reverse
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django_mysql.models import JSONField
from django.forms.models import model_to_dict
from posts.models import *
from django.contrib.auth.models import User
from django.db import models
from django_mysql.models import JSONField, Model
from posts.models import *
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


from django.db import models
from django_mysql.models import JSONField, Model
from posts.models import *
#from rest_framework import serializers #Later addtition with an argument in class Comment
def json_posts_default():
#    return {}
    return {"comments":[{"id":1,"c":"","li":"","ts":"","tag":[]}]}

class Comment(models.Model):
#    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
#    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
#    timestamp = models.DateTimeField(auto_now_add=True)
    comment_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('comment_type', 'object_id')
    content = JSONField(default=json_posts_default)
    class Meta:
        models.Index(fields=['comment_type','id']),
        db_table = 'comments'
    def __str__(self):
        return 'Post_ID Comments: '+self.post_id




#    def get_absolute_url(self):
#        return reverse("comments:thread", kwargs={"id": self.id})

#    def get_delete_url(self):
#        return reverse("comments:delete", kwargs={"id": self.id})

#   def children(self):  # replies
#        return Comment.objects.filter(parent=self)

#    @property
#    def is_parent(self):
#        if self.parent is not None:
#            return False
#        return True