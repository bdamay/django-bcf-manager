import os, sys
from datetime import datetime
proj_path = '/'.join(os.getcwd().split('\\')[:-2])+'/myproject'
# This is so Django knows where to find stuff.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
sys.path.append(proj_path)

# This is so my local_settings.py gets loaded.
os.chdir(proj_path)
# This is so models get loaded.

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

from django_bcf_manager.models import *
from django_bcf_manager import settings as app_settings
from django.conf import settings
from django_bcf_manager.lib import bcf_parser as bcfp



def run():
    file = os.path.join(app_settings.ASSETS_DIR,'BCF','examples','Annotations.bcfzip')  # testing purposes
    snapshots_dir = app_settings.SNAPSHOTS_DIR
    schemas_dir = os.path.join(app_settings.ASSETS_DIR,'BCF','Schemas')
    data = bcfp.extract_content_from_bcfzip(file, snapshots_dir, schemas_dir)
    print(data)
    pass


if __name__ == '__main__':
    start = datetime.now()
    print('start: ', start)
    run()
    end = datetime.now()
    print('end: ', end)

print('Ending')