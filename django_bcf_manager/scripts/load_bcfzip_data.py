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
from django_bcf_manager.lib import bcf_parser


def run():
    # Extract data
    file = os.path.join(app_settings.ASSETS_DIR,'BCF','examples','from_bcfier.bcfzip')  # testing purposes
    snapshots_dir = app_settings.SNAPSHOTS_DIR
    schemas_dir = os.path.join(app_settings.ASSETS_DIR,'BCF','Schemas')
    data = bcf_parser.extract_content_from_bcfzip(file, snapshots_dir, schemas_dir)

    #insert into model
    pj = Project.load_from_bcfdata(data['project'])
    for topic in data['topics']:
        Topic.load_from_bcfdata(topic)

    print(data)
    return


if __name__ == '__main__':
    start = datetime.now()
    print('start: ', start)
    run()
    end = datetime.now()
    print('end: ', end)

print('Ending')