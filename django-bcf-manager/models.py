from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ValidateModelMixin(object):
    def save(self, *args, **kwargs):
        """Call :meth:`full_clean` before saving."""
        self.full_clean()
        super(ValidateModelMixin, self).save(*args, **kwargs)


class Project(ValidateModelMixin, models.Model):
    project_id = models.CharField(max_length=255)
    name =models.CharField(max_length=255)
    extension_schema = models.CharField(max_length=255)
    created_by = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    modified_by = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    dt_creation = models.DateTimeField(auto_now_add=True)
    dt_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ' - '


class MarkupHeader(ValidateModelMixin, models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    created_by = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    modified_by = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    dt_creation = models.DateTimeField(auto_now_add=True)
    dt_modification = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name + ' - '


class MarkupHeaderFilenode(ValidateModelMixin, models.Model):
    markup_header = models.ForeignKey('MarkupHeader', on_delete=models.CASCADE)
    ifc_project= models.CharField(max_length=255, null=True, blank=True)
    ifc_spatial_structure_element = models.CharField(max_length=255, null=True, blank=True)
    is_external = models.BooleanField(default=True)
    filename =  models.CharField(max_length=255, null=True, blank=True)
    date =  models.DateField(null=True, blank=True)
    reference = models.CharField(max_length=255, null=True, blank=True)
    created_by = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    modified_by = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    dt_creation = models.DateTimeField(auto_now_add=True)
    dt_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ' - '


class Topic(ValidateModelMixin, models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    guid = models.CharField(max_length=255)
    topic_type = models.CharField(max_length=255)
    topic_status = models.CharField(max_length=255)
    created_by = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    modified_by = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    dt_creation = models.DateTimeField(auto_now_add=True)
    dt_modification = models.DateTimeField(auto_now=True)

class TopicReference(ValidateModelMixin, models.Model):
    reference = models.CharField(max_length=255)

class TopicPriority(ValidateModelMixin, models.Model):
    priority = models.CharField(max_length=255)

class TopicLabel(ValidateModelMixin, models.Model):
    priority = models.CharField(max_length=255)

class TopicStage(ValidateModelMixin, models.Model):
    priority = models.CharField(max_length=255)


class TopicNode(ValidateModelMixin, models.Model):
    topic =  models.ForeignKey('Topic', on_delete=models.CASCADE)
    reference_link = models.ManyToManyField('TopicReference')
    title = models.CharField(max_length=255)
    priority = models.ForeignKey('TopicPriority', null=True, blank=True, on_delete=models.SET_NULL)
    index = models.IntegerField(null=True, blank=True)
    labels =  models.ManyToManyField('TopicLabel')
    creation_date = models.DateTimeField()
    creation_author = models.CharField(max_length=255)
    modified_date = models.DateTimeField(null=True, blank=True)
    modified_author = models.CharField(max_length=255,null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    assigned_to = models.CharField(max_length=255,null=True, blank=True)
    description =  models.CharField(max_length=2048,null=True, blank=True)
    stage =  models.ManyToManyField('TopicStage')