import os
from django.conf import settings

SNAPSHOTS_DIR = os.path.join(settings.MEDIA_ROOT,'snapshots')
ASSETS_DIR = os.path.join(settings.BASE_DIR,'django_bcf_manager','assets')