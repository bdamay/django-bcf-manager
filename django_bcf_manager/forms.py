from django import forms
from django_bcf_manager.models import *


class BootstrapModelForm(forms.ModelForm):
    """
    Class intermédiaire pour ajouter les attributs de class bootstrap form-control
    """
    def __init__(self, *args, **kwargs):
        super(BootstrapModelForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class':'form-control form-control-sm',
                'autofocus':'',
                'placeholder':self.fields[field].label,
                'title':self.fields[field].label
            })

class BCFFileForm(BootstrapModelForm):
    class Meta:
        model = BcfFile
        fields = ['file']