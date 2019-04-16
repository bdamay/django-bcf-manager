from django.db import models
from django.contrib.auth.models import User

from django_bcf_manager.lib import bcf_parser
from django_bcf_manager import settings as app_settings
import os
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class ModelMixin(object):
    """
    Mixin methods for my Model classes
    """
    def save(self, *args, **kwargs):
        """ always Call `full_clean` method when saving."""
        self.full_clean()
        super(ModelMixin, self).save(*args, **kwargs)

    def attrs(self):
        return [(key, self.__dict__[key]) for key in self.__dict__ if key != '_state']


class Project(ModelMixin, models.Model):
    project_id = models.CharField(max_length=255)  # spec from BuildingSmart
    name = models.CharField(max_length=255, null=True)  # spec
    extension_schema = models.CharField(max_length=255, null=True,
                                        blank=True)  # spec is not optionnal in 2.1 but optionnal in BCF2.0 so i let it null
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    dt_creation = models.DateTimeField(auto_now_add=True)
    dt_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(
            self.id) + ': ' + self.name + ' - pid: ' + self.project_id + ' created_at ' + str(
            self.dt_creation) + ' - modified ' + str(self.dt_modification)

    @staticmethod
    def load_from_bcfdata(project_data):
        """
        Use this if you have to create an object from data as formatted by bcf_parser (xmlschema.to_dict)
        If project already exists, it will be modified
        :param project_data: dictionnary of project data parsed from bcfzip with bcf_parser
        :return: new Project object if not existing else the project updated
        """
        project_id = project_data['Project']['@ProjectId']

        project = Project.objects.filter(project_id=project_id)
        project = Project() if project.count() == 0 else project[0]

        project.project_id = project_id
        project.name = project_data['Project']['Name']
        project.extension_schema = project_data['ExtensionSchema']
        project.save()
        return project


class BcfFile(ModelMixin, models.Model):
    """
    Main source for BCF data - start with BCFFile to populate Topic data in model
    """
    name = models.CharField(max_length=255, blank=True)   # default calculated with file name ?
    file= models.FileField(upload_to='bcf')
    project = models.ForeignKey('Project', on_delete=models.CASCADE, blank=True, null=True)  # Populate after registration
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    dt_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + '(uploaded ' + str(self.dt_creation)+')'

    def clean(self):
        self.name = str(self.file)

    def handlePostRequest(self,request):
        if 'file' in request.FILES:
            self.file = request.FILES['file']
        self.summary_data = ifc.get_summary_data()  # get json qtys (raises if qty not present)
        self.save()
        pass

@receiver(post_save, sender=BcfFile)
def bcffile_post_save(sender, **kwargs):
    """
    After saving examine if we have to load bcf
    Might be better to move this code somewhere else ?
    """
    snapshots_dir = app_settings.SNAPSHOTS_DIR
    schemas_dir = os.path.join(app_settings.ASSETS_DIR, 'BCF', 'Schemas')
    filepath = kwargs['instance'].file.path
    data = bcf_parser.extract_content_from_bcfzip(filepath, snapshots_dir, schemas_dir)

    # insert into model
    pj = Project.load_from_bcfdata(data['project'])
    for topic in data['topics']:
        Topic.load_from_bcfdata(topic)



class Topic(ModelMixin, models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    guid = models.CharField(max_length=255)  # spec
    topic_type = models.CharField(max_length=255, null=True, blank=True)  # spec
    topic_status = models.CharField(max_length=255, null=True, blank=True)  # spec 2.1
    reference_link = models.ManyToManyField('TopicReference')  # spec element
    title = models.CharField(max_length=255)  # spec element
    priority = models.ForeignKey('TopicPriority', null=True, blank=True, on_delete=models.SET_NULL)  # spec element
    index = models.IntegerField(null=True, blank=True)  # spec element
    labels = models.ManyToManyField('TopicLabel')  # spec element
    creation_date = models.CharField(max_length=255, null=True, blank=True)  # spec element (ISO char)
    creation_author = models.CharField(max_length=255)  # spec element
    modified_date = models.CharField(max_length=255, null=True, blank=True)  # spec element (ISO char)
    modified_author = models.CharField(max_length=255, null=True, blank=True)  # spec element
    due_date = models.DateTimeField(null=True, blank=True)  # spec element
    assigned_to = models.CharField(max_length=255, null=True, blank=True)  # spec element
    description = models.CharField(max_length=2048, null=True, blank=True)  # spec element
    stage = models.ManyToManyField('TopicStage')  # spec element
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    dt_creation = models.DateTimeField(auto_now_add=True)
    dt_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.guid + ':  ' + self.topic_status + ' - pid ' + self.project.project_id + ' - ' + self.title


    @staticmethod
    def load_from_bcfdata(topic_data):
        """
        Use this if you have to create an object from data as formatted by bcf_parser (xmlschema.to_dict)
        If project already exists, it will be modified
        :param Topic: dictionnary of topic data parsed from bcfzip with bcf_parser
        :return: new Topic object if not existing else the Topic updated
        """
        project_id = topic_data['project_id']
        project = Project.objects.filter(project_id=project_id)
        if project.count() == 0:
            raise (Exception('no project match for this topic'))

        guid = topic_data['Topic']['@Guid']
        topic = Topic.objects.filter(guid=guid)
        topic = Topic() if topic.count() == 0 else topic[0]

        topic.project = project[0]
        topic.guid = guid
        topic.topic_type = topic_data['Topic']['@TopicType'] if '@TopicType' in topic_data['Topic'] else ''
        topic.topic_status = topic_data['Topic']['@TopicStatus'] if '@TopicStatus' in topic_data['Topic'] else ''
        # TODO ? topic.reference_link
        topic.title = topic_data['Topic']['Title']
        # TODO topic.priority = topic_data['Topic']['Priority'] if 'Priority' in topic_data['Topic'] else None
        topic.index = int(topic_data['Topic']['Index']) if 'Index' in topic_data['Topic'] else 0
        # TODO topic.labels = topic_data['Topic']['Priority'] if 'Priority' in topic_data['Topic']
        topic.creation_date = topic_data['Topic']['CreationDate']
        topic.creation_author = topic_data['Topic']['CreationAuthor']
        topic.modified_date = topic_data['Topic']['ModifiedDate'] if 'ModifiedDate' in topic_data['Topic'] else ''
        topic.modified_author = topic_data['Topic']['ModifiedAuthor'] if 'ModifiedAuthor' in topic_data['Topic'] else ''

        topic.save()

        return topic


class TopicReference(ModelMixin, models.Model):
    reference = models.CharField(max_length=255)


class TopicPriority(ModelMixin, models.Model):
    priority = models.CharField(max_length=255)


class TopicLabel(ModelMixin, models.Model):
    priority = models.CharField(max_length=255)


class TopicStage(ModelMixin, models.Model):
    priority = models.CharField(max_length=255)


class MarkupHeaderFilenode(ModelMixin, models.Model):
    """
    No MarkupHeader class as it contains no attributes - i choose to implement only the MarkupFileNode  in relation with Topic
    """
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE)
    ifc_project = models.CharField(max_length=255, null=True, blank=True)
    ifc_spatial_structure_element = models.CharField(max_length=255, null=True, blank=True)
    is_external = models.BooleanField(default=True)
    filename = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    reference = models.CharField(max_length=255, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+')
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+')
    dt_creation = models.DateTimeField(auto_now_add=True)
    dt_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ' - '
