from django.db import models, transaction
from django.core.exceptions import ValidationError
from django.template import Template, Context, loader

# Create your models here.
import re
from datetime import datetime as dt


import uuid
from . import *


from .base import *
from .bcf import *