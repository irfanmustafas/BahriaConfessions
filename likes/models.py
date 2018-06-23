from django.db import models
from django_mysql.models import JSONField, Model
from posts.models import *
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

def json_posts_default():
    return  dict
#    return {"likes":[{"id":1}]}
class ObjLike(models.Model):
#    object_id = models.ForeignKey(on_delete=models.CASCADE)
    like_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('like_type', 'object_id')
    like_count= models.IntegerField(default=0)
    content = JSONField(default=json_posts_default())
#    timestamp = models.DateTimeField(auto_now_add=True)
    class Meta:
        models.Index(fields=['like_type','id']),
        db_table = 'objlikes'
    def __str__(self):
        return 'object_id : '+self.object_id+'likes : '+self.like_count