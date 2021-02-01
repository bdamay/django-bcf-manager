from django.contrib.auth.models import User
from . import *

class CustomUserCreatedFk(models.ForeignKey):
    def contribute_to_class(self, cls, name, private_only=False, **kwargs):
        super().contribute_to_class(cls, name, private_only=False, **kwargs)
        self.remote_field.related_name = "_".join(re.findall('[A-Z][^A-Z]*', cls.__name__))+'_creator'

class CustomUserModifiedFk(models.ForeignKey):
    def contribute_to_class(self, cls, name, private_only=False, **kwargs):
        super().contribute_to_class(cls, name, private_only=False, **kwargs)
        self.remote_field.related_name = "_".join(re.findall('[A-Z][^A-Z]*', cls.__name__))+'_modifier'

class ModelBase(models.Model):
    """ Abstract class for dealing with Users and dates """
    class Meta:
        abstract = True

    # created_by = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)  TODO find a way to differenciate related_names here
    dt_creation = models.DateTimeField(auto_now_add=True)
    dt_modification = models.DateTimeField(auto_now=True)
    created_by = CustomUserCreatedFk(User, on_delete=models.PROTECT,  blank=True, related_name='%(class)s')
    modified_by = CustomUserModifiedFk(User, on_delete=models.PROTECT,  blank=True,  related_name='%(class)s')

    @transaction.atomic
    def save(self, *args, **kwargs):
        if self.created_by_id is None:
            self.created_by = User.objects.all()[0]    # default user
        if self.modified_by_id is None:
            self.modified_by = User.objects.all()[0]
        self.full_clean()  # TODO provoque un double passage sur clean quand on modifie dans l'admin  => comportement à éviter ?
        super(ModelBase, self).save(*args, **kwargs)

    # def attrs(self):
    #     return [(key, self.__dict__[key]) for key in self.__dict__ if key != '_state']

    def clean(self):
        """ Do here whatever you want to do before saving """
        pass


    @property
    def username(self):
        return self.created_by.username

    @property
    def user_mod(self):
        return User.objects.get(id=self.modified_by).username


