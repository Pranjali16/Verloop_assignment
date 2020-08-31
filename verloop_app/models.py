from django.db import models
from django.contrib.postgres.fields import ArrayField


class BaseModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Story(BaseModel):
    """ Story Model"""
    title = models.CharField(max_length=500, blank=True, null=True)
    sentences = ArrayField(models.CharField(max_length=500), blank=True, null=True)
    paragraphs = ArrayField(models.CharField(max_length=1000), blank=True, null=True)
    offset = models.PositiveIntegerField(default=0, blank=True)

    def __str__(self):
        return "%s %s" % (self.title, self.created_at)
